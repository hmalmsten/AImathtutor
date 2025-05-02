import { useState, useRef, useEffect } from 'react';
import Header from "./components/Header";
import Footer from "./components/Footer";
import FinishButton from './components/FinishButton';
import FeedbackForm from "./components/FeedbackForm";
import Dialogue from "./components/Dialogue";
import ConversationDisplay from "./components/ConversationDisplay"
import TaskDescription from './components/TaskDescription';
import RecipeDescriptionForm from './components/RecipeDescriptionForm';
import TutorialPopUp from './components/TutorialPopUp';
import SurveyButton from './components/SurveyButton'
import "./index.css";

const App = () => {
  const [isFinished, setIsFinished] = useState(false); 
  const [messages, setMessages] = useState([])
  const [isFinishClicked, setIsFinishClicked] = useState(false);
  const [isRatingSubmitted, setIsRatingSubmitted] = useState(false);
  const [isDisabled, setIsDisabled] = useState(false);
  const [recipeDescription, setRecipeDescription] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const viewPointRef = useRef(null);
  
  useEffect(() => {
    if (isFinished) {
      if (viewPointRef.current) {
        viewPointRef.current.scrollIntoView({ behavior: "smooth", block: "center"});
      }
    }
  }, [isFinished]);

  const addMessage = (message) => {
    setMessages(prevMessages => prevMessages.concat(message));
  };

  const toggleFinish = () => {
    setIsFinished(!isFinished);
    setIsFinishClicked(!isFinishClicked);
  }
  
  return (
    <>
      <Header />
      <TaskDescription />
      <SurveyButton />
      {/* <TutorialPopUp /> */}
      <RecipeDescriptionForm recipeDescription={recipeDescription} setRecipeDescription={setRecipeDescription} messages={messages} isDisabled={isDisabled} setIsDisabled={setIsDisabled} setIsLoading={setIsLoading} addMessage={addMessage}/>
      <div className="main-interaction">
        {(isRatingSubmitted || isFinishClicked) && (
          <div className="main-interaction-overlay"> </div>
        )}
        <Dialogue isLoading={isLoading} setIsLoading={setIsLoading} recipeDescription={recipeDescription} messages={messages} addMessage={addMessage} />
        <ConversationDisplay isLoading={isLoading} setIsLoading={setIsLoading} recipeDescription={recipeDescription} isDisabled={isDisabled} messages={messages} addMessage={addMessage} />
      </div>
      <FinishButton isFinishClicked={isFinishClicked} isRatingSubmitted={isRatingSubmitted} toggleFinish={toggleFinish} />
      {isFinished && <FeedbackForm viewPointRef={viewPointRef} isRatingSubmitted={isRatingSubmitted} setIsRatingSubmitted={setIsRatingSubmitted}/>}
      <Footer />
    </>
  );
};

export default App;
