import './App.css';
import logo from './icons/logo.svg';
import { HashRouter as Router, Routes, Route, Link } from "react-router-dom";
import Search from '../../searchify/src/components/search/search';
import Result from '../../searchify/src/components/result/result';


function App() {
  return (
    <Router>
      <div className="app-container">
        <header className="app-header">
            <img id='logo' src={logo} alt="logo" />
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
