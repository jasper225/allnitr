export default function Quiz() {
    return (
        <div className="summary">
            <h3>Summary</h3>
            <p>{summary}</p>

            <h4>Key Points</h4>
            <ul>
                {bullets.map((bullet, index) => (
                    <li key={index}>{bullet}</li>
                ))}
            </ul>
        </div>
    )
}