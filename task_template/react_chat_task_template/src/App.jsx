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

    const tryParseJSON = (jsonString) => {
        try {
            return JSON.parse(jsonString);
        } catch (err) {
            return null;
        }
    };
    
    
    const parseDeepJSON = (input, maxDepth = 5) => {
        let result = input;
        let depth = 0;
      
        while (typeof result === "string" && depth < maxDepth) {
            const trimmed = result.trim();
        
            if (trimmed.startsWith("{") && trimmed.endsWith("}")) {
                const parsed = tryParseJSON(trimmed);
                if (parsed !== null) {
                    result = parsed;
                    depth++;
                    continue;
                }
            }
      
            break;
        }
      
        return result;
    };

    const parsedAIResponse = (rawResponse) => {
      const deepParsed = parseDeepJSON(rawResponse); 
      const finalText = parseDeepJSON(deepParsed.text); 
    
      return {
        text: finalText.text || "",
        userSteps: finalText.userSteps || [],
        theory: finalText.theory || "",
      };
    };
    

    const handleMessage = async (userInput) => {
        const newMessages = [...messages, { sender: "User", text: userInput }];
        setMessages(newMessages);
        setLoading(true);

      try {
          const aiResponse = await taskService.submitUserInput(userInput);
          console.log("AI RESPONSE: " + JSON.stringify(aiResponse));

          //const rawText = aiResponse.text;
          //const parsed = parseDeepJSON(rawText);
          
          /*const aiTextResponse = {
            text: parsed?.text || rawText,
            userSteps: parsed?.userSteps || [],
            theory: parsed?.theory || "",
          };  */       
          
          const aiTextResponse = parsedAIResponse(aiResponse);

          console.log("PARSED AI RESPONSE:", aiTextResponse);
        
          setMessages([...newMessages, { sender: "AI", text: aiTextResponse.text }]);
          setTheory(prevTheory => prevTheory + "\n" + (aiTextResponse.theory || "")); //setTheory(aiTextResponse.theory || ""); 
          setSteps(prevSteps => [...prevSteps, ...(aiTextResponse.userSteps || [])]); //setSteps(aiTextResponse.userSteps || []); 

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
