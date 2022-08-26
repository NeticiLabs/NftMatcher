// //把REACT jsx拿来渲染？
// import React from 'react';
// import ReactDOM from 'react-dom/client';
// import App from './app.js';
  
// ReactDOM.render(
//     <React.StrictMode>
//       <App />
//     </React.StrictMode>,
//     document.getElementById('root')
// );

import React from 'react';
import ReactDOM from 'react-dom/client';

function Hello(props) {
  return <h1>Hello World!</h1>;
}

const root = ReactDOM.createRoot(document.getElementById("root"));

root.render(<Hello />);