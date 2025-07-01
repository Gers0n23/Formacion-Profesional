import { getUsers, createUser, updateUser, deleteUser } from '../../lib/db';

export default async function handler(req, res) {
  switch (req.method) {
    case 'GET':
      const users = await getUsers();
      res.status(200).json(users);
      break;
    case 'POST':
      const newUser = await createUser(req.body);
      res.status(201).json(newUser);
      break;
    case 'PUT':
      const updatedUser = await updateUser(req.body);
      res.status(200).json(updatedUser);
      break;
    case 'DELETE':
      await deleteUser(req.body.id);
      res.status(204).end();
      break;
    default:
      res.setHeader('Allow', ['GET', 'POST', 'PUT', 'DELETE']);
      res.status(405).end(`Method ${req.method} Not Allowed`);
  }
}
