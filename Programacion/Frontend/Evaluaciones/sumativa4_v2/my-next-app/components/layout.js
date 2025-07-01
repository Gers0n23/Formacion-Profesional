// File: /my-next-app/components/layout.js

import React from 'react';
import Header from './header';
import Footer from './footer';
import { CartProvider } from '../context/CartContext';

export default function Layout({ children }) {
  return (
    <CartProvider>
    <div className="flex flex-col min-h-screen">
      <Header />
      <main className="flex-grow">{children}</main>
      <Footer />
    </div>
    </CartProvider>
  );
} 