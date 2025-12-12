import { createContext, useContext, useState } from 'react';

const StudyContext = createContext();

export function StudyProvider({ children }) {
    const [rawText, setRawText] = useState('');
    const [summary, setSummary] = useState('');
    const [bullets, setBullets] = useState([]);
    const [quiz, setQuiz] = useState(null);

    return (
        <StudyContext.Provider value={{ rawText, setRawText, summary, setSummary, bullets, setBullets, quiz, setQuiz }}>
            {children}
        </StudyContext.Provider>


    );
}

export function useStudy() {
    return useContext(StudyContext);
}