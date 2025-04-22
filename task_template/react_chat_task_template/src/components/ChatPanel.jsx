import { useState, useRef, useEffect } from "react";
import 'katex/dist/katex.min.css';
import Latex from 'react-latex-next';

const ChatPanel = ({ messages, loading, onHandleMessage }) => {
    const [userInput, setUserInput] = useState("");
    const inputRef = useRef(null);
    const chatEndRef = useRef(null);

    useEffect(() => {
        chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
    }, [messages, loading]);

    const handleInput = () => {
        if (inputRef.current) {
            setUserInput(inputRef.current.innerText);
        }
    };

    const handleSend = () => {
        if (!userInput.trim()) return;

        onHandleMessage(userInput);
        
        if (inputRef.current) {
            inputRef.current.innerText = "";
        }
    };

    const handleKeyDown = (e) => {
        if (e.key === "Enter" && !e.shiftKey) {
            e.preventDefault();
            handleSend();
        }
    };

    return (
        <div className="dialogue-wrapper">
            <h2>Conversation</h2>
            <div className="chat-panel">
                <div className="chat-history">
                    {messages.map((msg, index) => (
                        <div key={index} className={`message ${msg.sender.toLowerCase()}`}>
                            <strong>{msg.sender}: </strong><Latex>{msg.text}</Latex>
                        </div>
                    ))}
                    {loading && <p><em>Loading...</em></p>}
                    <div ref={chatEndRef} />
                </div>

                <div 
                    className="chat-input"
                    contentEditable
                    ref={inputRef}
                    onInput={handleInput}
                    onKeyDown={handleKeyDown}
                    placeholder="Type your message here..."
                />
                <button 
                    className="send-btn" 
                    onClick={handleSend}>
                    Send
                </button>

            </div>
        </div>
    );
};

export default ChatPanel;
