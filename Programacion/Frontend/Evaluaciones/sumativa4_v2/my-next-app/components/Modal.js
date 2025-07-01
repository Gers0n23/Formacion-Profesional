import Image from 'next/image';
import { useState } from 'react';

function Modal({ product, onClose, addToCart }) {
  const [quantity, setQuantity] = useState(1);

  const handleChangeQuantity = (event) => {
    setQuantity(parseInt(event.target.value));
  };

  return (
    <div className="fixed inset-0 flex items-center justify-center z-50 bg-opacity-50 bg-gray-900">
      <div className="relative bg-white rounded-lg p-8 flex flex-col md:flex-row">
        <button className="absolute top-3 right-3" onClick={onClose}>
          <Image
            src="/assets/salir.png"
            alt="Cerrar modal"
            width={20}
            height={20}
          />
        </button>
        <div className="flex-none">
          <Image
            src={`/juegos/${product.image}`}
            alt={product.title}
            width={300}
            height={300}
          />
        </div>
        <div className="flex-grow ml-0 md:ml-4 mt-4 md:mt-0">
          <h3 className="text-xl font-semibold mt-2">{product.name}</h3>
          <p className="text-gray-600">{product.description}</p>
          <p className="mt-2">Disponibilidad: {product.availability}</p>
          <p>Ubicación: {product.location}</p>
          <p className="text-xl font-semibold mt-2">Precio: {product.price}</p>
          <div className="flex items-center mt-4">
            <label htmlFor="quantity">Cantidad:</label>
            <input
              type="number"
              id="quantity"
              min="1"
              value={quantity}
              onChange={handleChangeQuantity}
              className="mx-2 border rounded p-2"
            />
            <button
              className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
              onClick={() => {
                addToCart(product, quantity);
                onClose();
              }}
            >
              Agregar al carrito
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Modal;
