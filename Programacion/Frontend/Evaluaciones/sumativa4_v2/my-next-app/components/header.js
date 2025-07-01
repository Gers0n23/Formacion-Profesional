import Image from 'next/image';
import { useState } from 'react';
import { useCart } from '../context/CartContext';
import CartModal from './CartModal';
import AuthModal from './AuthModal';

export default function Header() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [showCart, setShowCart] = useState(false);
  const [showAuth, setShowAuth] = useState(false); // Añadir estado para el modal de autenticación
  const { cart } = useCart();

  const totalItems = cart.reduce((total, item) => total + item.quantity, 0);

  const handleAuthSuccess = () => {
    setIsLoggedIn(true);
  };

  return (
    <header className="bg-gray-800 text-white py-4">
      <div className="container mx-auto flex justify-between items-center">
        <h1 className="text-2xl font-bold">
          <span className="flex items-center">
            <Image src="/assets/inacaplogo2.jpg" alt="INACAPLudi_logo" width={50} height={50} />
            <span className="ml-2">INACAP Ludi</span>
          </span>
        </h1>
        <nav>
          <ul className="flex space-x-4">
            <li>
              <button 
                className="flex flex-col items-center"
                onClick={() => setShowAuth(true)} // Mostrar el modal de autenticación
              >
                <Image src="/assets/login_user.png" alt="Login" width={50} height={50} />
                <span>{isLoggedIn ? 'Logout' : 'Login'}</span>
              </button>
            </li>
            <li>
              <button 
                className="flex flex-col items-center"
                onClick={() => setShowCart(true)}
              >
                <Image src="/assets/cart-9.png" alt="Cart" width={50} height={50} />
                <span>{totalItems}</span>
              </button>
            </li>
          </ul>
        </nav>
      </div>

      {showCart && (
        <CartModal onClose={() => setShowCart(false)} />
      )}
      
      {showAuth && (
        <AuthModal onClose={() => setShowAuth(false)} onAuthSuccess={handleAuthSuccess} />
      )}
    </header>
  );
}
