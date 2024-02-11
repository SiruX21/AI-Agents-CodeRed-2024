import React, { useState } from 'react';
import SpeechRecognition, { useSpeechRecognition } from 'react-speech-recognition';
import './Dictaphone.css'; // Import CSS for styling
import Navbar from "./components/navbar";
import Home from "./pages";
import index from "./pages/index";
import Voice from "./pages/voice";
import Teacher from "./pages/teacher"
import {
  BrowserRouter as Router,
  Routes,
  Route,
} from "react-router-dom";
const Dictaphone = () => {
  const {
    transcript,
    listening,
    resetTranscript,
    browserSupportsSpeechRecognition
  } = useSpeechRecognition();
  const [uploading, setUploading] = useState(false);

  const downloadTranscript = () => {
    const element = document.createElement('a');
    const file = new Blob([transcript], { type: 'text/plain' });
    element.href = URL.createObjectURL(file);
    element.download = 'transcript.txt';
    document.body.appendChild(element);
    element.click();
  };

  const generateRandomName = () => {
    const timestamp = Date.now();
    const randomString = Math.random().toString(36).substring(2, 8); // Generate a random string
    return `transcript_${timestamp}_${randomString}.txt`;
  };

  const handleUpload = async () => {
    try {
      setUploading(true);
      const formData = new FormData();
      const fileName = generateRandomName(); // Generate a random name for the file
      const file = new Blob([transcript], { type: 'text/plain' });
      formData.append('file', file, fileName);

      const response = await fetch('http://127.0.0.1:6050/upload', {
        method: 'POST',
        body: formData,
      });

      if (response.ok) {
        console.log('Files uploaded successfully');
      } else {
        console.error('Failed to upload files');
      }
    } catch (error) {
      console.error('Error uploading files:', error);
    } finally {
      setUploading(false);
    }
  };

  if (!browserSupportsSpeechRecognition) {
    return <span className="error-msg">Browser doesn't support speech recognition.</span>;
  }

  return (
    <div className="Dictaphone">
             <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/voice" element={<Voice />} />
        <Route path="/teacher" element={<Teacher />} />
      </Routes>
    </Router>
      <p className="status">Microphone: {listening ? 'on' : 'off'}</p>
      <div className="button-group">
        <button className="control-button" onClick={SpeechRecognition.startListening}>Start</button>
        <button className="control-button" onClick={SpeechRecognition.stopListening}>Stop</button>
        <button className="control-button" onClick={resetTranscript}>Reset</button>
        <button className="control-button" onClick={downloadTranscript}>Download Transcript</button>
        <button className="control-button" onClick={handleUpload} disabled={uploading}>
          {uploading ? 'Uploading...' : 'Upload Transcript'}
        </button>
      </div>
      <p className="transcript">{transcript}</p>
    </div>
  );
};

export default Dictaphone;
