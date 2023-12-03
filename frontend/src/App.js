import React from "react";
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { Nav } from "./components/Nav";
import { Home } from "./components/Home.js";
import { Music } from "./components/Music.js";
import { RoutePlan } from "./components/RoutePlan.js";

export class App extends React.Component {

  render() {
    return (
      <Router>
        {/* <div className="route-container">
          <Nav />
          <Routes>
            <Route exact path="/" element={<Home />} />
            <Route path="/plan" element={<RoutePlan />} />
            <Route path="/music" element={<Music />} />
          </Routes>
        </div> */}
        
      </Router>
    );
  }
}

export default App;
