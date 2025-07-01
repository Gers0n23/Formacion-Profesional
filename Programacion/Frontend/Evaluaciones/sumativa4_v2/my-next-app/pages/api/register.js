import { getUsers, createUser } from '../../lib/db';

export default async function handler(req, res) {
  if (req.method === 'POST') {
    const { username, email, password, real_name } = req.body;

    if (!username || !email || !password) {
      return res.status(400).json({ success: false, message: 'Por favor, completa todos los campos requeridos.' });
    }

    try {
      // Verificar si el usuario ya existe
      const users = await getUsers();
      const existingUser = users.find(user => user.username === username || user.email === email);

      if (existingUser) {
        return res.status(409).json({ success: false, message: 'El usuario o correo electrónico ya existe.' });
      }

      // Crear el nuevo usuario
      const newUser = await createUser({
        username,
        email,
        password,
        real_name: real_name || username // Usa el username como real_name si no se proporciona
      });

      // Omitir la contraseña en la respuesta por seguridad
      const { password: _, ...userWithoutPassword } = newUser;

      res.status(201).json({ success: true, user: userWithoutPassword });
    } catch (error) {
      console.error('Error durante el registro:', error);
      res.status(500).json({ success: false, message: 'Error del servidor: ' + error.message });
    }
  } else {
    res.status(405).json({ message: 'Método no permitido' });
  }
}

