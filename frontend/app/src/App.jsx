import ListManager from './components/ListManager';

function App() {
  return (
    <div>
      <header className="App-header">
        <p>¡Bienvenido! Aquí puedes gestionar tus listas de tareas.</p>
      </header>
      <h1>Gestor de Listas y Tareas</h1>
      <ListManager />
      <footer className="App-footer">
        <p>Copyright &copy; 2025 Franco Vannucci Fernandez, All Rights Reserved.</p>
      </footer>
    </div>
  );
}

export default App;

