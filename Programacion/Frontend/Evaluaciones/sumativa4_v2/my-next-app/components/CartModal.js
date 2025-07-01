import { useCart } from '../context/CartContext';
import Image from 'next/image';

function CartModal({ onClose }) {
  const { cart, removeFromCart, updateQuantity } = useCart();

  return (
    <div className="fixed inset-0 flex items-center justify-center z-50 bg-opacity-50 bg-gray-900">
      <div className="relative bg-white rounded-lg p-8 max-w-lg w-full text-black"> {/* Añadido text-black */}
        <button className="absolute top-3 right-3" onClick={onClose}>
          <Image
            src="/assets/salir.png"
            alt="Cerrar modal"
            width={20}
            height={20}
          />
        </button>
        <h2 className="text-2xl font-bold mb-4">Carrito de Compras</h2>
        {cart.length === 0 ? (
          <p className="text-gray-600">El carrito está vacío</p>
        ) : (
          cart.map((item) => (
            <div key={item.id} className="flex justify-between items-center mb-4">
              <span>{item.name}</span>
              <div className="flex items-center">
                <input 
                  type="number" 
                  min="1" 
                  value={item.quantity} 
                  onChange={(e) => updateQuantity(item.id, parseInt(e.target.value))}
                  className="w-16 mr-2 p-1 border rounded"
                />
                <button 
                  onClick={() => removeFromCart(item.id)}
                  className="bg-red-500 text-white px-2 py-1 rounded"
                >
                  Eliminar
                </button>
              </div>
            </div>
          ))
        )}
        <button 
          onClick={onClose}
          className="mt-4 bg-blue-500 text-white px-4 py-2 rounded"
        >
          Cerrar
        </button>
      </div>
    </div>
  );
}

export default CartModal;
