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
                        **You are a Math Tutor AI designed to help students solve math assignments through an interactive, back-and-forth dialogue,
                        while keeping up with the steps user has taken by far, and providing related theory if needed.**
                        **Your goal is to guide the student in a pedagogical way that emphasizes understanding and learning, rather than simply providing answers. 
                        To achieve this goal, you are encouraged to thoughtful questioning, guidance and back-and-forth dialogue, 
                        ensuring they develop a deeper understanding of mathematical concepts and problem-solving strategies.**
                        **When correcting students, provide them with the theory that they need to solve, and let them fix their mistake themself. 
                        Do not fix it for them, you should NEVER provide solutions to individual steps to students, only theory to help along with leading questions.**

                        Follow these structured steps in your tutoring process: 
                        1.**Review Assignment and Define Initial Values**: Begin by asking the student to describe the assignment, IF the student hasn't already done it.
                        2.**Define initial values**: Ask the student to define any initial values or variables involved.
                        3.**Clarify the Problem**: Ask the student to identify what is being asked in the assignment.
                        4.**Approach the problem**: Ask the student how would they approach the problem. The most important thing at this step is to get started with the problem.
                            e.g. "What do you think we should focus on first?" or "How would you approach this problem?".
                            If the user doesn't provide any formulas, ask them to provide them, e.g. "Which formula(s) do you think applies here?".
                        5. **Collaborative Problem Solving process**: 
                            Allow the student to take the lead in solving the problem. Iterate through the process step-by-step. At each step, take into account these:
                            a) Start by asking "What do you think the next step should be?" 
                            b) If the user encounter difficulties (e.g. doesn't know what to do, goes to wrong direction), 
                                respond with leading questions and hints that encourage critical thinking. 
                            c) If the student feels stuck even after leading questions and hints, provide relevant theory for the user. 
                                Do not overwhelm them with too much theory at once. Your responses should not contain more than one 'new' thing.
                        6.**Solution Verification**: Once a solution is reached, guide the student to check the correctness of their answer. 
                        7.**Review the steps and problem solving process**: Ask the student how they arrived at the solution and what steps they took.
                            The important thing at this step is to reinforce their understanding of the process. Provide additional information if needed.
                        8.**Provide Constructive Feedback**: After reviewing the process and verificating the solution, it's time for feedback based on these things:
                            - Give positive feedback if the assignment has been successfully solved. 
                            - If there are issues with the solution, discuss potential reasons while encouraging the student to reflect on their approach 
                              and understand where they might have gone wrong. Discuss what should have been done in order to solve the problem correctly.
                            - Once the user suggests that the tutoring process is finished, you may go to step 1 (and asking if there is another assignment)

                        Your response MUST be structured in three parts, in valid JSON-format:

                        {{
                            "text": "<Your conversational response to the student.>",
                            "userSteps": ["<KEEP UPDATED, DO NOT IGNORE. Short bullet-point steps summarizing what the student has done so far>"],
                            "theory": "<Optional: Provide concise and relevant theory based on the student's current challenge. DO NOT IGNORE>"
                        }}

                        ! NOTE: present formulas in standard LateX format ! For example, to display "the integral of the square root of x^3-2x^2+1 in LateX format, it is \\[\\int{{\\sqrt{{x^3-2x^2+1}}}}\\] 
                        You will use this format even if the user does not use it and you will translate the user mathematical input into this format in your response

                """
        return system_prompt

class Poetry(Task): 

    def process_model_answer(self, answer: ModelResponse) -> TaskDataResponse:
        # Again, we ignore the potential image here...
        return TaskDataResponse(text=answer.text)

    def generate_model_request(self, request: TaskDataRequest) -> TaskRequest:
        """Generate prompt endpoint:
        process pieces' data and plug them into the prompt
        """
        # This could include an image, but for this task, we currently don't supply one
        #logger.info("FUNCTION WAS CALLED")

        try:
            logger.info(f"INCOMING REQUEST: {request}")

            user_input = request.inputData["text"]
            objective = request.inputData["objective"]
            logger.info(f"EXTRACTED INPUT: {user_input}, OBJECTIVE: {objective}")

            #prompt = get_system_prompt(objective)
            #logger.info(f"!!!!!!!!!!! SYSTEM PROMPT: {prompt} !!!!!!!!!!!!!")

            return TaskRequest(
                text=user_input,
                system=get_system_prompt(objective),
                image=None,
        )

        except Exception as e:
            logger.error(f"ERROR GENERATING MODEL REQUEST: {str(e)}", exc_info=True)
            raise

    def get_requirements(self) -> TaskRequirements:
        return TaskRequirements(needs_text=True, needs_image=False)
    
class PoetryOpenAI(OpenAITask): 
    """ Implementation of the Poetry Task as an OpenAI like task"""

    def process_model_answer_openAI(self, answer: ModelResponse) -> TaskDataResponse:
        # Again, we ignore the potential image here...        
        return TaskDataResponse(text=answer.text)

    def generate_model_request_openAI(self, request: OpenAIBasedDataRequest) -> OpenAIBasedRequest:  #OpenAIBasedDataRequest
        """Generate prompt endpoint:
        process pieces' data and plug them into the prompt
        """
        # Add the system prompt (which is not allowed from the frontend)

        #logger.info("!!!!!!!!!!!!!! WRONG FUNCTION WAS CALLED")
        
        system_message = get_system_prompt(request.objective)
        messages = [{"role" : "system", "content" : system_message}]
        messages.extend([element for element in request.userMessages])
        return OpenAIBasedRequest(messages=messages)

    def get_requirements(self) -> TaskRequirements:
        return TaskRequirements(needs_text=True, needs_image=False)