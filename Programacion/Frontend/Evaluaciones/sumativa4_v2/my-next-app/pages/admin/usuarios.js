import { useState, useEffect } from 'react';

export default function AdminUsers() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    fetchUsers();
  }, []);

  async function fetchUsers() {
    const res = await fetch('/api/users');
    const data = await res.json();
    setUsers(data);
  }

  async function handleCreateUser(event) {
    event.preventDefault();
    const form = event.target;
    const username = form.username.value;
    const password = form.password.value;

    await fetch('/api/users', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username, password }),
    });

    form.reset();
    fetchUsers();
  }

  // Implementa las funciones handleUpdateUser y handleDeleteUser

  return (
    <div className="container mx-auto py-8">
      <h1 className="text-3xl font-bold mb-4">Administrar Usuarios</h1>
      
      <form onSubmit={handleCreateUser} className="mb-8">
        <input type="text" name="username" placeholder="Username" required className="mr-2 p-2 border" />
        <input type="password" name="password" placeholder="Password" required className="mr-2 p-2 border" />
        <button type="submit" className="bg-blue-500 text-white px-4 py-2 rounded">Crear Usuario</button>
      </form>

      <table className="w-full">
        <thead>
          <tr>
            <th>ID</th>
            <th>Username</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          {users.map(user => (
            <tr key={user.id}>
              <td>{user.id}</td>
              <td>{user.username}</td>
              <td>
                {/* Agrega botones para actualizar y eliminar usuarios */}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}