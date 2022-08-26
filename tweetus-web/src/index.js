import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import Forms from './components/Forms';
import App from './App';
import reportWebVitals from './reportWebVitals';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    {/* <App /> */}
    <Forms />      
  </React.StrictMode>
);

// here index.html is the one which is rendering in the web page
// in that we have one div tag which is provided with one ID="root" this ID is linking to the 
// src/index.js here it is rendering the Forms.js


// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
