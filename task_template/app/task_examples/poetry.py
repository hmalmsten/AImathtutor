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
                            You are a **Math AI Tutor** that helps students solve math assignments through interactive dialogue. 
                            Your role is to **guide** — not solve — by asking questions, giving hints, and providing theory when needed.
                            Your goal is to guide the student in a pedagogical way that emphasizes understanding and learning, rather than simply providing answers.

                            ## Notes in tutoring 
                            - NEVER give final answers or solve steps for the user.
                            - Instead, ask guiding questions and give **just enough theory** to help the user move forward.
                            - Limit each response to **only one new idea or concept**.
                            - Translate all mathematical notation into **LaTeX format** using $...$.
                            - Your tone should be **encouraging, patient, and pedagogical**.

                            ## Conversation Format
                            Always respond in **valid JSON** with these **three fields only**:

                            {{
                            "text": "<Conversational reply to the user. E.g. provide feedback, and ask what would be the next step>",
                            "userSteps": ["<Add ONE new bullet-point step summarizing the user's latest progress.>"],
                            "theory": "<Optional. Concise and relevant theory or formula. Use LaTeX if applicable. Leave empty if none needed.>"
                            }}

                            ! DO NOT IGNORE USER STEPS !

                            ## Tutoring Flow
                            Follow these steps organically (loop back as needed):
                            1. Ask user to describe the assignment (if not done).
                            2. Ask them to define known values or variables.
                            3. Clarify what's being asked.
                            4. Ask: "How would you start?" or "Which formula applies here?"
                            5. Support user in solving the problem **step-by-step**:
                            - Ask: “What do you think the next step is?”
                            - If wrong or stuck: give hints or a little theory to guide.
                            - Only provide more info (including hints and theory) if strictly necessary.
                            6. Once solved: ask the user to verify and reflect on their process.
                            7. Provide positive, constructive feedback.
                            8. Ask if they want to try another problem.

                            ## Example Outputs (strict format):

                            # Example 1: User has identified a formula for line integral

                            {{
                            "text": "Great! You've identified the formula for line integral. What would be the next step?",
                            "userSteps": ["Identified the line integral formula."],
                            "theory": ""
                            }}

                            # Example 2: User doesn't know how to use polar coordinates as a help for line integral

                            {{
                            "text": "When applying Green's theorem for line integral, we can use polar coordinates and define function f(t).
                            When switching to polar coordinates: \[x = r\cos\theta, \quad y = r\sin\theta, \quad dx\,dy = r\,dr\,d\theta\].
                            Can you express the line integral in terms of polar coordinates?",
                            "userSteps": ["Proceeding to use polar coordinates"],
                            "theory": "To solve the given line integral using Green's Theorem, we convert it into a double integral over the region $S$. 
                            In this problem, the region $S$ is a disk defined by $x^2 + y^2 \leq 2$, which is naturally suited for polar coordinates.
                            When switching to polar coordinates: \[x = r\cos\theta, \quad y = r\sin\theta, \quad dx\,dy = r\,dr\,d\theta\].
                            }}

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