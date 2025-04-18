const ConversationDisplay = ({ messages, loading }) => {
    return (
        <div className="chat-space-wrapper">
            <h2>Conversation</h2>
            <div className="chat-space">
                {messages.map((msg, index) => (
                  <p key={index}><strong>{msg.sender}:</strong> {msg.text}</p>
                ))}
                {loading && <p><em>Loading...</em></p>}
            </div>
        </div>
    );
  };

export default ConversationDisplay;