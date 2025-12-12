import Summary from '../components/Summary.jsx';
import Quiz from '../components/Quiz.jsx';
import { useStudy } from '../context/StudyContext.jsx';

export default function StudySession() {
    const { summary, quiz, bullets } = useStudy();

    return (
        <div className="study-session">
            <h2>Study Material</h2>

            <Summary summary={summary} bullets={bullets} />
            <Quiz quiz={quiz} />
        </div>

    );
}