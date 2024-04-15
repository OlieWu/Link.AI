import './App.css';
import Login from './components/Login';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import logo from './icons/logo.svg';
import Search from './components/search/search';
import Result from './components/result/result';

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
