import { useState, useRef, useEffect } from 'react';

import Header from "./components/Header";
import Footer from "./components/Footer";
import FinishButton from './components/FinishButton';
import FeedbackForm from "./components/FeedbackForm";
import ChatPanel from "./components/ChatPanel";
import StepsAndTheoryDisplay from "./components/StepsAndTheoryDisplay";

import taskService from "./services/task"; 

import "./index.css";

const App = () => {
    const [messages, setMessages] = useState([]); 
    const [steps, setSteps] = useState([]);
    const [theory, setTheory] = useState("");

    const [isFinished, setIsFinished] = useState(false); 
    const [isFinishClicked, setIsFinishClicked] = useState(false);
    const [isRatingSubmitted, setIsRatingSubmitted] = useState(false);

    const [loading, setLoading] = useState(false);
    const viewPointRef = useRef(null);
    
    useEffect(() => {
      if (isFinished) {
        if (viewPointRef.current) {
          viewPointRef.current.scrollIntoView({ behavior: "smooth", block: "center"});
        }
      }
    }, [isFinished]);

    const toggleFinish = () => {
      setIsFinished(!isFinished);
      setIsFinishClicked(!isFinishClicked);
    };


    const handleMessage = async (userInput) => {
        const newMessages = [...messages, { sender: "User", text: userInput }];
        setMessages(newMessages);
        setLoading(true);

      try {
          const aiResponse = await taskService.submitUserInput(userInput);
          console.log("AI RESPONSE: " + JSON.stringify(aiResponse));

          let aiTextResponse;
          try {
              if (
                  typeof aiResponse.text === "string" &&
                  aiResponse.text.trim().startsWith("{") &&
                  aiResponse.text.trim().endsWith("}")
              ) {
                  aiTextResponse = JSON.parse(aiResponse.text);
              } else {
                aiTextResponse = {
                  text: aiResponse.text,
                  userSteps: [],
                  theory: "",
                };
              }
          } catch (innerError) {
            console.error("Failed to parse AI response text:", innerError);
            setMessages([...newMessages, { sender: "AI", text: "Error: Couldn't parse the AI's response." }]);
            return;
          }

          console.log("AI TEXT RESPONSE: " + JSON.stringify(aiTextResponse));
        
          setMessages([...newMessages, { sender: "AI", text: aiTextResponse.text }]);
          setTheory(aiTextResponse.theory || ""); 
          setSteps(aiTextResponse.userSteps || []); 

          console.log("MESSAGES: " + JSON.stringify(messages));
          console.log("THEORY: " + JSON.stringify(aiTextResponse.theory));
          console.log("STEPS: " + JSON.stringify(aiTextResponse.userSteps));

      } catch (error) {
          console.error("Error sending message:", error);
          setMessages([...newMessages, { sender: "AI", text: "Error: Could not get a response." }]);

      } finally {
          setLoading(false);
      }
  
    };
    
    return (
        <>
            <Header />
            <div className="main-interaction">
                {(isRatingSubmitted || isFinishClicked) && (
                  <div className="main-interaction-overlay"> </div>
                )}
                <ChatPanel messages={messages} loading={loading} onHandleMessage={handleMessage} />
                <StepsAndTheoryDisplay steps={steps} theory={theory} loading={loading} />
            </div>
            <FinishButton isFinishClicked={isFinishClicked} isRatingSubmitted={isRatingSubmitted} toggleFinish={toggleFinish} />
            {isFinished && <FeedbackForm viewPointRef={viewPointRef} isRatingSubmitted={isRatingSubmitted} setIsRatingSubmitted={setIsRatingSubmitted}/>}
            <Footer />
        </>
    );
};

export default App;
