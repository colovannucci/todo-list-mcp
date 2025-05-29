import { useEffect, useState } from "react";

function BackendMessage() {
    const [msg, setMsg] = useState("Cargando...");

    useEffect(() => {
        fetch("http://localhost:8000/api/hello")
            .then(res => res.json())
            .then(data => setMsg(data.message))
            .catch(() => setMsg("No se pudo conectar al backend"));
    }, []);

    return (
        <div className="card">
            <p>Mensaje del backend: <strong>{msg}</strong></p>
        </div>
    );
}

export default BackendMessage;
// This component fetches a message from the backend API and displays it.
// It uses the useEffect hook to perform the fetch operation when the component mounts.