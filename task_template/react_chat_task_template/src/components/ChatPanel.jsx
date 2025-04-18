import { useState, useRef, useEffect } from "react";

const ChatPanel = ({ messages, loading, onSendMessage }) => {
    const [userInput, setUserInput] = useState("");
    const inputRef = useRef(null);
    const chatEndRef = useRef(null);

    const handleInput = () => {
        if (inputRef.current) {
            setUserInput(inputRef.current.innerText);
        }
    };

    const handleSend = () => {
        if (!userInput.trim()) return;

        onSendMessage(userInput);
        setUserInput("");
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

    useEffect(() => {
        chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
    }, [messages, loading]);

    return (
        <div className="dialogue-wrapper">
            <h2>Conversation</h2>
            <div className="chat-panel">
                <div className="chat-history">
                    {messages.map((msg, index) => (
                        <div key={index} className={`message ${msg.sender.toLowerCase()}`}>
                            <strong>{msg.sender}:</strong> {msg.text}
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
