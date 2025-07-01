import { getUsers } from '../../lib/db';

export default async function handler(req, res) {
  if (req.method === 'POST') {
    const { email, password } = req.body;

    if (!email || !password) {
      return res.status(400).json({ success: false, message: 'Por favor, ingresa correo y contraseña.' });
    }

    try {
      const users = await getUsers();
      const user = users.find(user => user.email === email);

      if (user && password === user.password) {
        // Aquí puedes agregar lógica para generar un token de sesión si es necesario
        res.status(200).json({ success: true });
      } else {
        res.status(401).json({ success: false, message: 'Credenciales inválidas' });
      }
    } catch (error) {
      console.error('Error durante la autenticación:', error);
      res.status(500).json({ success: false, message: 'Error del servidor' });
    }
  } else {
    res.status(405).json({ message: 'Método no permitido' });
  }
}
