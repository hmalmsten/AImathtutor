import 'katex/dist/katex.min.css';
import Latex from 'react-latex-next';

const StepsAndTheoryDisplay = ({ steps, theory, loading }) => {
    return (
        <div className="steps-theory-wrapper">
            <h2>Steps and Theory</h2>

            <div className="right-panel">
                <div className="steps-space">
                  <h3>Steps Taken:</h3>
                    {steps.length > 0 ? (
                        <ul>
                            {steps.map((step, index) => (
                                <li key={index}> <Latex>{step}</Latex></li>
                            ))}
                        </ul>
                    ) : (
                        <p> </p> 
                    )}
                </div>

                <div className="theory-space">
                  <h3>Theory:</h3>
                        {theory ? (
                            <Latex>{theory}</Latex>
                        ) : 
                            <p> </p>}
                </div>
            </div>

        </div>
    );
  };


  /*steps.map(step => <li>{step}</li>)*/

export default StepsAndTheoryDisplay;