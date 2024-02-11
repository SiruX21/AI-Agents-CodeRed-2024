import { useState, useEffect } from "react";
import "./App.css";
import lens from "./assets/lens.png";
import loadingGif from "./assets/loading.gif";
// Filename - App.js
 
import React from "react";
import Navbar from "./components/navbar";
import {
    BrowserRouter as Router,
    Routes,
    Route,
} from "react-router-dom";
import Home from "./pages";
import index from "./pages/index";
import Voice from "./pages/voice";
import Teacher from "./pages/teacher";
function App() {
  const [prompt, updatePrompt] = useState(undefined);
  const [loading, setLoading] = useState(false);
  const [answer, setAnswer] = useState(undefined);

  useEffect(() => {
    if (prompt != null && prompt.trim() === "") {
      setAnswer(undefined);
    }
  }, [prompt]);
  const sendPrompt = async (event) => {
    if (event.key !== "Enter") {
      return;
    }
  
    try {
      setLoading(true);
    
      const encodedPrompt = encodeURIComponent(prompt);
      const requestOptions = {
        method: "POST",
        headers: { "Content-Type": "application/json" },
      };
      
      const res = await fetch(`http://127.0.0.1:5051/run_agent?input_text=${encodedPrompt}`, requestOptions);
    
      if (!res.ok) {
        throw new Error("Something went wrong");
      }
    
      let finalAnswer = await res.text(); // Extract text directly
  
      // Extract everything after "action_input":"
      setAnswer(finalAnswer);
    } catch (err) {
      console.error(err, "err");
    } finally {
      setLoading(false);
    }
  };
  
  return (
    
    <div className="app">
      <div className="app-container">
      <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/voice" element={<Voice />} />
        <Route path="/teacher" element={<Teacher />} />
      </Routes>
    </Router>
        <h1 style={{ textAlign: 'center' }}>Teacher AI</h1> {/* Add this line */}
        <div className="spotlight__wrapper">
          <input
            type="text"
            className="spotlight__input"
            placeholder="Ask me anything..."
            disabled={loading}
            style={{
              backgroundImage: loading ? `url(${loadingGif})` : `url(${lens})`,
            }}
            onChange={(e) => updatePrompt(e.target.value)}
            onKeyDown={(e) => sendPrompt(e)}
          />
          <div className="spotlight__answer">{answer && <p>{answer}</p>}</div>
        </div>
      </div>

    </div>
    
  );
}
export default App;