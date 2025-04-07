import { useState, useRef, useEffect } from 'react';

import Header from "./components/Header";
import Footer from "./components/Footer";
import FinishButton from './components/FinishButton';
import FeedbackForm from "./components/FeedbackForm";
import Workspace from "./components/Workspace";
import ConversationDisplay from "./components/ConversationDisplay"

import taskService from "./services/task"; 

import "./index.css";

const App = () => {
    const [isFinished, setIsFinished] = useState(false); 
    const [isFinishClicked, setIsFinishClicked] = useState(false);
    const [isRatingSubmitted, setIsRatingSubmitted] = useState(false);
    const [messages, setMessages] = useState([]); 
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
            const aiResponse = await taskService.submitUserInput({ message: userInput });
            setMessages([...newMessages, { sender: "AI", text: aiResponse.response }]);
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
                <Workspace onSendMessage={sendMessage} />
                <ConversationDisplay messages={messages} loading={loading} />
            </div>
            <FinishButton isFinishClicked={isFinishClicked} isRatingSubmitted={isRatingSubmitted} toggleFinish={toggleFinish} />
            {isFinished && <FeedbackForm viewPointRef={viewPointRef} isRatingSubmitted={isRatingSubmitted} setIsRatingSubmitted={setIsRatingSubmitted}/>}
            <Footer />
        </>
    );
};

export default App;
