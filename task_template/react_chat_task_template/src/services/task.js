import axios from 'axios'

const baseUrl = "/api/v1/task"

const submitUserInput = async (newUserMessage) => {
  console.log("new user message on task service " + newUserMessage);

  try {
    const response = await axios.post(`${baseUrl}/process`, newUserMessage); 
    console.log("Response: " + response.data);
  } catch (e) {
    console.error("Error submitting user input:", e);
    throw new Error("Failed to get a response from the model.");
  }
  
  return response.data;
};

const finishTask = (rating) => {
  const ratingjson = {
    metrics: {
      rating: rating, 
      task_name: "placeholder" //change this to your task name
    }
  }
  const request = axios.post(`${baseUrl}/finish`, ratingjson)
  return request.then(response => response.data)
};

export default { 
  finishTask,
  submitUserInput
};