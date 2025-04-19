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


    const sendMessage = async (userInput) => {
        const newMessages = [...messages, { sender: "User", text: userInput }];
        setMessages(newMessages);
        setLoading(true);

      try {
          const aiResponse = await taskService.submitUserInput(userInput);
          const aiTextResponse = aiResponse.text;
          console.log("AI RESPONSE IN APP: " + JSON.stringify(aiResponse));
          console.log("AI RESPONSE TEXT IN APP: " + JSON.stringify(aiTextResponse.text));
          setMessages([...newMessages, { sender: "AI", text: aiTextResponse.text }]);
          setTheory(aiTextResponse.userSteps || []); 
          setSteps(aiTextResponse.theory || ""); 
          console.log("MESSAGES: " + messages);
          console.log("THEORY: " + theory);
          console.log("STEPS: " + steps);

      } catch (error) {
          console.error("Error sending message:", error);
          setMessages([...newMessages, { sender: "AI", text: "Error: Could not get a response." }]);

      } finally {
          setLoading(false);
      }

        
    };

    const handleAIResponse = async (newMessages, input) => {
        try {
            const aiResponse = await taskService.submitUserInput(input);
            setMessages([...newMessages, { sender: "AI", text: aiResponse.text }]);
            setTheory(aiResponse.userSteps || []); 
            setSteps(aiResponse.theory || ""); 

        } catch (error) {
            console.error("Error sending message:", error);
            setMessages([...newMessages, { sender: "AI", text: "Error: Could not get a response." }]);

        } finally {
            setLoading(false);
        }
    };


    /*           <Workspace onSendMessage={sendMessage} />
                <ConversationDisplay messages={messages} loading={loading} />*/
    
    return (
        <>
            <Header />
            <div className="main-interaction">
                {(isRatingSubmitted || isFinishClicked) && (
                  <div className="main-interaction-overlay"> </div>
                )}
                <ChatPanel messages={messages} loading={loading} onSendMessage={sendMessage} />
                <StepsAndTheoryDisplay steps={steps} theory={theory} loading={loading} />
            </div>
            <FinishButton isFinishClicked={isFinishClicked} isRatingSubmitted={isRatingSubmitted} toggleFinish={toggleFinish} />
            {isFinished && <FeedbackForm viewPointRef={viewPointRef} isRatingSubmitted={isRatingSubmitted} setIsRatingSubmitted={setIsRatingSubmitted}/>}
            <Footer />
        </>
    );
};

export default App;
