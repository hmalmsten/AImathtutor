import { useRef, useState } from "react";

const Workspace = ({ onSendMessage }) => {
    const [userInput, setUserInput] = useState("");
    const inputRef = useRef(null);

    const handleInput = (event) => {
        if (inputRef.current) {
            setUserInput(inputRef.current.innerText);
        }
    };

    const handleSend = () => {
        if (!userInput.trim()) {
            return;
        }
        onSendMessage(userInput); 
        setUserInput("");

        if (inputRef.current) {
            inputRef.current.innerText = ""; 
        }
    };

    return (
        <div className="dialogue-wrapper">
            <h2>Workspace</h2>
            <div 
                className="dialogue" 
                ref={inputRef}
                contentEditable="true"
                onInput={handleInput}
                placeholder="Type your message here..."
                style={{
                    minHeight: "50px",
                    outline: "none",
                    cursor: "text",
                }}
            ></div>
            <button onClick={handleSend}>Send</button>
        </div>
    );
};

export default Workspace;
