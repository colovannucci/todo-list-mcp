import { useEffect, useState } from 'react';
import { getItems, createItem, updateItem, deleteItem, completeItem, uncompleteItem } from '../api/items';

function TodoList({ listId }) {
  const [items, setItems] = useState([]);
  const [newTitle, setNewTitle] = useState('');
  const [newDescription, setNewDescription] = useState('');
  const [editItemId, setEditItemId] = useState(null);
  const [editTitle, setEditTitle] = useState('');
  const [editDescription, setEditDescription] = useState('');

  useEffect(() => {
    if (!listId) return;
    fetchItems();
  }, [listId]);

  const fetchItems = () => {
    getItems(listId)
      .then(res => setItems(res.data))
      .catch(console.error);
  };

  const handleAddItem = () => {
    if (!newTitle.trim()) return;
    createItem(listId, { title: newTitle, description: newDescription })
      .then(() => {
        setNewTitle('');
        setNewDescription('');
        fetchItems();
      })
      .catch(console.error);
  };

  const handleStartEdit = (item) => {
    setEditItemId(item.id);
    setEditTitle(item.title);
    setEditDescription(item.description);
  };

  const handleSaveEdit = (itemId) => {
    updateItem(listId, itemId, { title: editTitle, description: editDescription })
      .then(() => {
        setEditItemId(null);
        fetchItems();
      })
      .catch(console.error);
  };

  const handleDelete = (itemId) => {
    deleteItem(listId, itemId)
      .then(() => fetchItems())
      .catch(console.error);
  };

  const handleToggleComplete = (item) => {
    const action = item.completed ? uncompleteItem : completeItem;
    action(listId, item.id)
      .then(() => fetchItems())
      .catch(console.error);
  };

  return (
    <div>
      <h2>Tareas de la Lista {listId} {listName}</h2>
      {items.length === 0 ? (
        <p>📭 Esta lista no tiene tareas.</p>
      ) : (
        <ul>
          {items.map(item => (
            <li key={item.id} style={{ textDecoration: item.completed ? 'line-through' : 'none' }}>
              {editItemId === item.id ? (
                <>
                  <input value={editTitle} onChange={e => setEditTitle(e.target.value)} />
                  <input value={editDescription} onChange={e => setEditDescription(e.target.value)} />
                  <button onClick={() => handleSaveEdit(item.id)}>💾</button>
                  <button onClick={() => setEditItemId(null)}>✖️</button>
                </>
              ) : (
                <>
                  <strong>{item.title}</strong>: {item.description}
                  <button onClick={() => handleStartEdit(item)}>✏️</button>
                  <button onClick={() => handleToggleComplete(item)}>
                    {item.completed ? '↩️' : '✅'}
                  </button>
                  <button onClick={() => handleDelete(item.id)}>🗑️</button>
                </>
              )}
            </li>
          ))}
        </ul>
      )}
      <div>
        <input
          type="text"
          placeholder="Título del ítem..."
          value={newTitle}
          onChange={e => setNewTitle(e.target.value)}
        />
        <input
          type="text"
          placeholder="Descripción del ítem..."
          value={newDescription}
          onChange={e => setNewDescription(e.target.value)}
        />
        <button onClick={handleAddItem}>Agregar</button>
      </div>
    </div>
  );
}

export default TodoList;
