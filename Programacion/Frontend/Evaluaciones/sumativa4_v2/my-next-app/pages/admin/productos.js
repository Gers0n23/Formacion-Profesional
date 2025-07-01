import { useState, useEffect } from 'react';

export default function AdminProducts() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    fetchProducts();
  }, []);

  async function fetchProducts() {
    const res = await fetch('/api/products');
    const data = await res.json();
    setProducts(data);
  }

  async function handleCreateProduct(event) {
    event.preventDefault();
    const form = event.target;
    const product = {
      title: form.title.value,
      description: form.description.value,
      availability: form.availability.value,
      location: form.location.value,
      image: form.image.value,
    };

    await fetch('/api/products', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(product),
    });

    form.reset();
    fetchProducts();
  }

  async function handleUpdateProduct(productId) {
    const productToUpdate = products.find((product) => product.id === productId);
    // (Optional) Prompt user for updated product information

    const updatedProduct = {
      // Update the relevant product properties here based on user input or form data
      ...productToUpdate,
      title: 'Updated Title', // Example update
    };

    await fetch(`/api/products/${productId}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(updatedProduct),
    });

    fetchProducts(); // Update product list after successful update
  }

  async function handleDeleteProduct(productId) {
    if (window.confirm('¿Estás seguro de eliminar el producto?')) {
      await fetch(`/api/products/${productId}`, {
        method: 'DELETE',
      });

      fetchProducts(); // Update product list after successful deletion
    }
  }

  return (
    <div className="container mx-auto py-8">
      <h1 className="text-3xl font-bold mb-4">Administrar Productos</h1>

      <form onSubmit={handleCreateProduct} className="mb-8">
        <input type="text" name="title" placeholder="Título" required className="mr-2 p-2 border" />
        <input type="text" name="description" placeholder="Descripción" required className="mr-2 p-2 border" />
        <input type="number" name="availability" placeholder="Disponibilidad" required className="mr-2 p-2 border" />
        <input type="text" name="location" placeholder="Ubicación" required className="mr-2 p-2 border" />
        <input type="text" name="image" placeholder="Nombre de la imagen" required className="mr-2 p-2 border" />
        <button type="submit" className="bg-blue-500 text-white px-4 py-2 rounded">Crear Producto</button>
      </form>

      <table className="w-full">
        <thead>
          <tr>
            <th>ID</th>
            <th>Título</th>
            <th>Descripción</th>
            <th>Disponibilidad</th>
            <th>Ubicación</th>
            <th>Imagen</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          {products.map((product) => (
            <tr key={product.id}>
              <td>{product.id}</td>
              <td>{product.title}</td>
              <td>{product.description}</td>
              <td>{product.availability}</td>
              <td>{product.location}</td>
              <td>{product.image}</td>
              <td>
                <button onClick={() => handleUpdateProduct(product.id)} className="bg-green-500 text-white px-2 py-1 rounded mr-2">
                  Editar
                </button>
                <button onClick={() => handleDeleteProduct(product.id)} className="bg-red-500 text-white px-2 py-1 rounded">
                  Eliminar
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
