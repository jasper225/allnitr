import {BrowserRouter, Route, Routes} from "react-router-dom";
import Home from "./pages/Home.jsx";
import StudySession from "./pages/StudySession.jsx";

export default function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path ="/study" element={<StudySession />} />
            </Routes>
        </BrowserRouter>
    );
}
