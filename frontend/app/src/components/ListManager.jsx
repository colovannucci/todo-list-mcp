import { useEffect, useState } from 'react';
import { getAllLists, createList, deleteList, updateList } from '../api/lists';
import TodoList from './TodoList';

function ListManager() {
    const [lists, setLists] = useState([]);
    const [selectedListId, setSelectedListId] = useState(null);
    const [newListName, setNewListName] = useState('');

    useEffect(() => {
        fetchLists();
    }, []);

    const fetchLists = () => {
        getAllLists()
            .then(res => {
                setLists(res.data);
            })
            .catch(console.error);
    };

    const handleCreateList = () => {
        if (!newListName.trim()) return;
        createList({ name: newListName })
            .then(() => {
                setNewListName('');
                fetchLists();
            })
            .catch(console.error);
    };

    const handleDeleteList = (id) => {
        if (!window.confirm('¿Eliminar esta lista?')) return;
        deleteList(id)
            .then(() => {
                if (selectedListId === id) {
                    setSelectedListId(null);
                }
                fetchLists();
            })
            .catch(console.error);
    };

    const handleUpdateList = (id, name) => {
        const newName = prompt('Nuevo nombre de la lista:', name);
        if (newName && newName.trim()) {
            updateList(id, { name: newName.trim() })
                .then(fetchLists)
                .catch(console.error);
        }
    };

    return (
        <div>
            <div>
                <input
                    type="text"
                    placeholder="Nueva lista..."
                    value={newListName}
                    onChange={(e) => setNewListName(e.target.value)}
                />
                <button onClick={handleCreateList}>➕ Crear</button>
            </div>

            {lists.length > 0 ? (
                <>
                    <div>
                        <label htmlFor="list-select">Seleccionar lista:</label>
                        <select
                            id="list-select"
                            value={selectedListId || ''}
                            onChange={(e) => {
                                const val = e.target.value;
                                setSelectedListId(val === '' ? null : Number(val));
                            }}
                        >
                            <option value="">-- Selecciona una lista --</option>
                            {lists.map((list) => (
                                <option key={list.id} value={list.id}>
                                    {list.name}
                                </option>
                            ))}
                        </select>
                    </div>

                    {selectedListId && lists.find(l => l.id === selectedListId) && (
                        <div style={{ marginTop: '0.5rem' }}>
                            <button onClick={() => handleUpdateList(selectedListId, lists.find(l => l.id === selectedListId)?.name)}>
                                ✏️ Renombrar
                            </button>
                            <button onClick={() => handleDeleteList(selectedListId)}>
                                🗑️ Eliminar
                            </button>
                        </div>
                    )}
                </>
            ) : (
                <p>No hay listas disponibles. Crea una para comenzar.</p>
            )}

            {selectedListId ? (
                <TodoList listId={selectedListId} />
            ) : (
                <p>Por favor, selecciona una lista para continuar.</p>
            )}
        </div>
    );
}

export default ListManager;
// This component manages the lists, allowing users to create, delete, and select lists.
// It also renders the TodoList component for the selected list.