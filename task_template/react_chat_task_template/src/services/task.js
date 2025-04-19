import axios from 'axios'

const baseUrl = "/api/v1/task"

const submitUserInput = async (newUserMessage) => {
    console.log("new user message on task service " + newUserMessage);

    const inputObject = {
        inputData: {
          text: newUserMessage,
          objective: "math tutoring"
        }
      };

    try {
        const response = await axios.post(`${baseUrl}/process`, inputObject, {
            headers: {
                "Content-Type": "application/json",
                "Ocp-Apim-Subscription-Key": process.env.OPENAI_API_KEY
            }
        });
        //console.log("RESPONSE: " + JSON.stringify(response));
        //console.log("Response data: " + JSON.stringify(response.data));
        return response.data;

    } catch (e) {
        console.error("Error submitting user input:", e);
        throw new Error("Failed to get a response from the model.");
    }
};

const finishTask = (rating) => {
  const ratingjson = {
    metrics: {
      rating: rating, 
      task_name: "math tutoring" 
    }
  }
  const request = axios.post(`${baseUrl}/finish`, ratingjson)
  return request.then(response => response.data)
};

export default { 
  finishTask,
  submitUserInput
};