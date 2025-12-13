export default function Summary({ summary, bullets}) {
    if (!summary) {
        return <p>No summary available.</p>
    }
    
    
  return (
    <div>
      <h3>Summary</h3>
      <p>{summary}</p>

      {Array.isArray(bullets) && bullets.length > 0 && (
        <>
          <h4>Key Points</h4>
          <ul>
            {bullets.map((b, i) => (
              <li key={i}>{b}</li>
            ))}
          </ul>
        </>
      )}
    </div>
  );
}