import { useState } from 'react';
import Image from 'next/image';

function AuthModal({ onClose, onAuthSuccess }) {
  const [isLogin, setIsLogin] = useState(true);
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [realName, setRealName] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();
    setError('');

    const payload = isLogin
      ? { username, password }
      : { username, email, password, real_name: realName };

    try {
      const res = await fetch(`/api/${isLogin ? 'login' : 'register'}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
      });

      const data = await res.json();
      if (data.success) {
        onAuthSuccess(data.user);
        onClose();
      } else {
        setError(data.message || 'Error en la autenticación');
      }
    } catch (err) {
      console.error('Error durante la autenticación:', err);
      setError('Error de conexión');
    }
  };

  return (
    <div className="fixed inset-0 flex items-center justify-center z-50 bg-opacity-50 bg-gray-900">
      <div className="relative bg-white rounded-lg p-8 max-w-lg w-full text-black">
        <button className="absolute top-3 right-3" onClick={onClose}>
          <Image
            src="/assets/salir.png"
            alt="Cerrar modal"
            width={20}
            height={20}
          />
        </button>
        <h2 className="text-2xl font-bold mb-4">{isLogin ? 'Iniciar Sesión' : 'Registrarse'}</h2>
        {error && <p className="text-red-500 mb-4">{error}</p>}
        <form onSubmit={handleSubmit}>
          <div className="mb-4">
            <label htmlFor="username" className="block mb-1">Nombre de Usuario:</label>
            <input
              type="text"
              id="username"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              className="w-full border rounded p-2"
              required
            />
          </div>
          {!isLogin && (
            <>
              <div className="mb-4">
                <label htmlFor="email" className="block mb-1">Correo Electrónico:</label>
                <input
                  type="email"
                  id="email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  className="w-full border rounded p-2"
                  required
                />
              </div>
              <div className="mb-4">
                <label htmlFor="realName" className="block mb-1">Nombre Real:</label>
                <input
                  type="text"
                  id="realName"
                  value={realName}
                  onChange={(e) => setRealName(e.target.value)}
                  className="w-full border rounded p-2"
                  required
                />
              </div>
            </>
          )}
          <div className="mb-4">
            <label htmlFor="password" className="block mb-1">Contraseña:</label>
            <input
              type="password"
              id="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="w-full border rounded p-2"
              required
            />
          </div>
          <button
            type="submit"
            className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
          >
            {isLogin ? 'Iniciar Sesión' : 'Registrarse'}
          </button>
        </form>
        <button
          onClick={() => setIsLogin(!isLogin)}
          className="mt-4 text-blue-500"
        >
          {isLogin ? '¿No tienes una cuenta? Regístrate' : '¿Ya tienes una cuenta? Inicia sesión'}
        </button>
      </div>
    </div>
  );
}

export default AuthModal;