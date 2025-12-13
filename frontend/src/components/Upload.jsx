import { useState } from 'react';
import { uploadFile } from '../api/client';
import { useNavigate } from 'react-router-dom';
import { useStudy } from '../context/StudyContext.jsx';

export default function Upload() {
    const [file, setFile] = useState(null);
    const [loading, setLoading] = useState(false);
    const navigate = useNavigate();
    const { setRawText, setSummary, setBullets, setQuiz } = useStudy();

    async function handleUpload() {
        if (!file) return;
        setLoading(true);
        
        try {
        
        const data = await uploadFile(file);

        setRawText(data.raw_text);
        setSummary(data.summary);
        setBullets(data.bullets);
        setQuiz(data.quiz);

        setLoading(false);
        navigate('/study');
        } catch (error) {
            console.error(error);
            alert('Failed to upload file. Please try again.');
        }
        finally {
        setLoading(false);
        }
    }
    return (
        <div className="upload-container">
            <input type= "file" onChange ={e => setFile(e.target.files[0])} />
            <button onClick={handleUpload} disabled={loading}>
                {loading ? 'Uploading...' : 'Upload'}
            </button>
        </div>

    )
}