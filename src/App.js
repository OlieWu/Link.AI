import logo from './logo.svg';
import './App.css';
import Tenants from './components/tenantsTable';
import Input from './components/input';

function App() {
  return (
    <div>
      <h1>Leasing Office Tool</h1>
      <Input />
      <Tenants />
    </div>
  );
}

export default App;
