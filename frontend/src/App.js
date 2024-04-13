import logo from './logo.svg';
import './App.css';
import { HashRouter as Router, Routes, Route, Link } from "react-router-dom";
import Search from './components/search/search';
import Spotify from './components/spotify/spotify';
import Result from './components/result/result';

function App() {
  return (
    <Router>
      <div className="app-container">
      <header className="app-header">
          <h1>searchify</h1>
        </header>
        <main className="main-container">
          <Routes>
            <Route path="/" key="search" element={<Search />} />
            <Route path="/result" key="result" element={<Result />} />
          </Routes>
        </main>
        <footer className="app-footer">
          
        </footer>
      </div>
    </Router>
  );
}

export default App;
