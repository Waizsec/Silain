import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import App from './App.jsx';
import Dashboard from './Dashboard.jsx'; // Import the dashboard component
import './style.css';

// Assuming `App` is the index page
ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <Router>
      <Routes>
        {/* Define the route for index (home page) */}
        <Route path="/" element={<App />} />
        {/* Define the route for the dashboard */}
        <Route path="/dashboard" element={<Dashboard />} />
      </Routes>
    </Router>
  </React.StrictMode>,
);
