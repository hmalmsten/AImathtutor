import logging
from typing import Any, List
import json
from tasks.task_interface import Task, OpenAITask
from models import (
    TaskDataRequest,
    TaskRequest,
    TaskDataResponse,
    ModelResponse,
    TaskRequirements,
    OpenAIBasedDataRequest,
    OpenAIBasedRequest
)

logger = logging.getLogger(__name__)

def get_system_prompt(objective: str) -> str:
        """Generate response endpoint:
        generate the response based on given prompt and store the conversation
        in the history of the session (based on the session_id cookie)
        """

        system_prompt = f"""
                        You are a Math Tutor AI designed to help students solve math assignments through an interactive, back-and-forth dialogue. 
                        Your goal is to guide the student in a way that emphasizes understanding and learning, rather than simply providing answers.
                        Follow these structured steps in your tutoring process: 
                        1.**Review Assignment and Define Initial Values**: Begin by asking the student to describe the assignment, 
                            ensuring they articulate the problem and define any initial values or variables involved.
                        2.**Clarify the Problem**: Encourage the student to identify what is being asked in the assignment.
                            Prompt them to think about the methods they might use to solve the problem and what formulas are relevant. 
                            Use questions like, "What do you think we should focus on first?" or "Which formula do you think applies here?" 
                        3.**Collaborative Problem Solving**: Allow the student to take the lead in solving the problem. 
                            If they encounter difficulties, respond with leading questions and hints that encourage critical thinking. 
                            For instance, ask, "What do you think the next step should be?" or " Can you recall the theory behind this concept?" 
                            If the student feels stuck, revisit the relevant theory, asking them to explain it in their own words before applying it to the problem.
                        4.**Solution Verification**: Once a solution is reached, guide the student to check the correctness of their answer. 
                            Ask them how they arrived at the solution and what steps they took, reinforcing their understanding of the process.
                        5.**Provide Constructive Feedback**: After reviewing the solution, give positive feedback if the assignment has been successfully solved. 
                            If there are issues with the solution, discuss potential reasons why it may not be working, 
                            encouraging the student to reflect on their approach and understand where they might have gone wrong. 

                        Additional instructions:
                        1. Remember, your primary goal is to facilitate the student's learning process through thoughtful questioning, guidance and back-and-forth dialogue, 
                            ensuring they develop a deeper understanding of mathematical concepts and problem-solving strategies.
                        2. Your responses should always end with a question.
                        3. Only provide responses with one question at a time. The students should not be overloaded with too much information at once.
                        4. When correcting students, provide them with the theory that they need to solve, and give them an opportunity to fix their mistake themself. 
                        Do not fix it for them, you should not provide solutions to individual steps to students, only theory to help.
            """
        return system_prompt

class Poetry(Task): #RENAMED FROM Poetry


    def process_model_answer(self, answer: ModelResponse) -> TaskDataResponse:
        # Again, we ignore the potential image here...
        return TaskDataResponse(text=answer.text)

    def generate_model_request(self, request: TaskDataRequest) -> TaskRequest:
        """Generate prompt endpoint:
        process pieces' data and plug them into the prompt
        """
        # This could include an image, but for this task, we currently don't supply one
        logger.info(request)

        """linetag = "COMMENT" if request.inputData["comment"] else "NEWLINE"
        poemline = f"POEM : {json.dumps(request.inputData['poem'])}"
        newline = f"{linetag} : {request.text}"""

        # FOR MATH TUTOR:
        user_input = request.text

        """return TaskRequest(
            text=f"{poemline} \n{newline}",
            system=get_system_prompt(request.objective),
            image=None,
        )"""

        # FOR MATH TUTOR:
        return TaskRequest(
        text=user_input,
        system=get_system_prompt(request.objective),
        image=None,
    )

    def get_requirements(self) -> TaskRequirements:
        return TaskRequirements(needs_text=True, needs_image=False)
    
class PoetryOpenAI(OpenAITask): # RENAMED FROM PoetryOpenAI
    """ Implementation of the Poetry Task as an OpenAI like task"""

    def process_model_answer_openAI(self, answer: ModelResponse) -> TaskDataResponse:
        # Again, we ignore the potential image here...        
        return TaskDataResponse(text=answer.text)

    def generate_model_request_openAI(self, request: OpenAIBasedDataRequest) -> OpenAIBasedRequest:
        """Generate prompt endpoint:
        process pieces' data and plug them into the prompt
        """
        # Add the system prompt (which is not allowed from the frontend)
        system_message = get_system_prompt(request.objective)
        messages = [{"role" : "system", "content" : system_message}]
        messages.extend([element for element in request.userMessages])
        return OpenAIBasedRequest(messages=messages)
        

    def get_requirements(self) -> TaskRequirements:
        return TaskRequirements(needs_text=True, needs_image=False)