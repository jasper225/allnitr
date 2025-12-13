export default function Quiz({ quiz }) {
  if (!quiz || (!quiz.mcq?.length && !quiz.tf?.length)) {
    return <p>No quiz generated yet.</p>;
  }

  return (
    <div>
      <h3>Quiz</h3>

      {quiz.mcq?.map((q, i) => (
        <div key={`mcq-${i}`}>
          <p>{q.question}</p>
          <ul>
            {q.options.map((opt, j) => (
              <li key={j}>{opt}</li>
            ))}
          </ul>
        </div>
      ))}

      {quiz.tf?.map((q, i) => (
        <p key={`tf-${i}`}>{q.question}</p>
      ))}
    </div>
  );
}
