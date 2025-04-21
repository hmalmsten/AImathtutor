import { useState, useRef, useEffect } from "react";
import 'katex/dist/katex.min.css';
import { InlineMath, BlockMath } from 'react-katex';

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

    return (
        <div className="dialogue-wrapper">
            <h2>Conversation</h2>
            <div className="chat-panel">
                <div className="chat-history">
                    {messages.map((msg, index) => (
                        <div key={index} className={`message ${msg.sender.toLowerCase()}`}>
                            <strong>{msg.sender}: </strong>
                            <span
                                dangerouslySetInnerHTML={{
                                    __html: renderMath(msg.text), 
                                }}
                            />
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
