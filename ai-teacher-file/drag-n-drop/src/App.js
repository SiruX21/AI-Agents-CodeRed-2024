import React, { useCallback, useState } from 'react';
import { useDropzone } from 'react-dropzone';
import './App.css';
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
function App() {
  const [files, setFiles] = useState([]);

  const onDrop = useCallback(acceptedFiles => {
    setFiles(acceptedFiles);
    uploadFiles(acceptedFiles);
  }, []);

  const uploadFiles = async files => {
    const formData = new FormData();
    files.forEach(file => {
      formData.append('file', file);
    });

    try {
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
    }
  };

  const { getRootProps, getInputProps } = useDropzone({ onDrop });

  return (
    <div className="App">
       <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/voice" element={<Voice />} />
        <Route path="/teacher" element={<Teacher />} />
      </Routes>
    </Router>
      <div {...getRootProps({ className: 'dropzone' })}>
        <input {...getInputProps()} />
        <p>Drag 'n' drop some files here, or click to select files</p>
      </div>
      <aside>
        <h4>Uploaded files:</h4>
        <ul>
          {files.map(file => (
            <li key={file.name}>
              {file.name} - {file.size} bytes
            </li>
          ))}
        </ul>
      </aside>
    </div>
  );
}

export default App;
