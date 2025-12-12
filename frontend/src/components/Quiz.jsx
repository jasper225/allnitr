

export default function Quiz() {
    if (!quiz) return null;
    return (
        <div className="quiz">
            <h3>Quiz</h3>

            <h4>Multiple Choice</h4>
            {quiz.multiple_choice.map((q, index) => (
                <div key={index} className="quiz-question">
                    <p>{q.question}</p>
                    <ul>
                        {q.options.map((option, i) => (
                            <li key={i}>{option}</li>
                        ))}
                    </ul>
                </div>
            ))}

            <h4>True / False</h4>
            {quiz.true_false.map((q, index) => (
                <div key={index} className="quiz-question">
                    <p>{q.question}</p>
                    <ul>
                        <li>True</li>
                        <li>False</li>
                    </ul>
                </div>
            ))}
        </div>
    )
}