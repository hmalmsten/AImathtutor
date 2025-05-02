import { useState, useRef, useEffect } from "react";
import Header from "./components/Header";
import Footer from "./components/Footer";
import FinishButton from "./components/FinishButton";
import FeedbackForm from "./components/FeedbackForm";
import SurveyButton from './components/SurveyButton'
import "./index.css";

const App = () => {
  const [isFinished, setIsFinished] = useState(false);
  const [isFinishClicked, setIsFinishClicked] = useState(false);
  const [isRatingSubmitted, setIsRatingSubmitted] = useState(false);
  const viewPointRef = useRef(null);

  useEffect(() => {
    if (isFinished) {
      if (viewPointRef.current) {
        viewPointRef.current.scrollIntoView({
          behavior: "smooth",
          block: "center",
        });
      }
    }
  }, [isFinished]);

  const toggleFinish = () => {
    setIsFinished(!isFinished);
    setIsFinishClicked(!isFinishClicked);
  };

  return (
    <>
      <Header />
      <SurveyButton />
      <div className="main-interaction">
        {(isRatingSubmitted || isFinishClicked) && (
          <div className="main-interaction-overlay"> </div>
        )}
        <iframe
          src="/godot_games/tangram/index.html"
          width="90%"
          height="100%"
        />
      </div>
      <FinishButton
        isFinishClicked={isFinishClicked}
        isRatingSubmitted={isRatingSubmitted}
        toggleFinish={toggleFinish}
      />
      {isFinished && (
        <FeedbackForm
          viewPointRef={viewPointRef}
          isRatingSubmitted={isRatingSubmitted}
          setIsRatingSubmitted={setIsRatingSubmitted}
        />
      )}
      <Footer />
    </>
  );
};

export default App;
