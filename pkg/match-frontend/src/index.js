// //把REACT jsx拿来渲染？
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './app.js';

// ReactDOM.render(
//     <React.StrictMode>
//       <App />
//     </React.StrictMode>,
//     document.getElementById('root')
// );


const root = ReactDOM.createRoot(document.getElementById("root"));

root.render(<App />);