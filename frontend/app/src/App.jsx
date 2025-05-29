import { useState } from 'react';
import ListManager from './components/ListManager';
import TodoList from './components/TodoList';

function App() {
  const [selectedListId, setSelectedListId] = useState(null);

  return (
    <div>
      <header className="App-header">
        <p>¡Bienvenido! Aquí puedes gestionar tus listas de tareas.</p>
      </header>
      <h1>Gestor de Listas y Tareas</h1>
      <ListManager />
      <footer className="App-footer">
        <p>&copy; 2025 Franco vannucci. Todos los derechos reservados.</p>
      </footer>
    </div>
  );
}

export default App;

