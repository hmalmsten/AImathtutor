import 'katex/dist/katex.min.css';
import { InlineMath, BlockMath } from 'react-katex';

const renderMath = (text) => {
    const regexInline = /\$(.*?)\$/g; // Inline LaTeX: $...$
    const regexBlock = /\$\$(.*?)\$\$/g; // Block LaTeX: $$...$$
  
    text = text.replace(regexBlock, (match, latex) => {
      return `<BlockMath math="${latex}" />`;  
    });
  
    text = text.replace(regexInline, (match, latex) => {
      return `<InlineMath math="${latex}" />`; 
    });
  
    return text;
};

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
                                <li key={index}>
                                   <span
                                        dangerouslySetInnerHTML={{
                                            __html: renderMath(step), 
                                        }}
                                    />
                                </li>
                            ))}
                        </ul>
                    ) : (
                        <p> </p> 
                    )}
                </div>

                <div className="theory-space">
                  <h3>Theory:</h3>
                        {theory ? (
                            <span
                                dangerouslySetInnerHTML={{
                                    __html: renderMath(theory),
                                }}
                            />
                        ) : <p> </p>}
                </div>
            </div>

        </div>
    );
  };


  /*steps.map(step => <li>{step}</li>)*/

export default StepsAndTheoryDisplay;