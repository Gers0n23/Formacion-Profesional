import { getProducts, createProduct, updateProduct, deleteProduct } from '../../lib/db';

export default async function handler(req, res) {
  switch (req.method) {
    case 'GET':
      const products = await getProducts();
      res.status(200).json(products);
      break;
    case 'POST':
      const newProduct = await createProduct(req.body);
      res.status(201).json(newProduct);
      break;
    case 'PUT':
      const updatedProduct = await updateProduct(req.body);
      res.status(200).json(updatedProduct);
      break;
    case 'DELETE':
      await deleteProduct(req.body.id);
      res.status(204).end();
      break;
    default:
      res.setHeader('Allow', ['GET', 'POST', 'PUT', 'DELETE']);
      res.status(405).end(`Method ${req.method} Not Allowed`);
  }
}
