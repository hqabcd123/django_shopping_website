import logo from './logo.svg';
import './App.css';
import React, { Component, useEffect, useState } from "react";

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// export default App;


//---------------------------------------------------------------------------------------

const img1 = require('./static/media/hio01.jpg').default

const Canvas = () => {
  const [context, setContext] = useState(null)

  const [loaded, setLoaded] = useState(false)

  useEffect(()=>{
    const canvas =document.getElementById("canvas")
    const canvasContext = canvas.getContext("2d")
    setContext(canvasContext)
  }, [])
  useEffect(()=>{
    if (context!==null)
    {
      const img = new image()
      img.src = "img.jpg"
    }
  })
}

function App()
{
  return (
    <div className="app">
      <h3>
        hello
      </h3>
      <br/>
      <input type="text" />
      <br/>
      <img src={img1} />
    </div>
  )
}

export default App;