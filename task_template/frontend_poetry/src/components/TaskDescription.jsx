const TaskDescription = () => {
  return (
    <div className="task-description">
      <h2>🖋️ Poetry task</h2>
      <h3>📜 Rules</h3>
      <ol>
        <li>The user choose a theme for the poem. After that, the first line is generated by the AI</li>
        <li>The user and AI take turns to write the poem</li>
        <li>There are two input field: the first one is for adding a new poemline, the second one is for sending the model a comment</li>
        <li>The poem is finished when it reaches the 9-line limit</li>
      </ol>
    </div>
  );
};

export default TaskDescription;
