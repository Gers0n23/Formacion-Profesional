// pages/_app.js

import '../styles/global.css';
import Layout from '../components/layout';
import { CartProvider } from '../context/CartContext';

function MyApp({ Component, pageProps }) {
  return (
    <CartProvider>
    <Layout>
      <Component {...pageProps} />
    </Layout>
    </CartProvider>
  );
}

export default MyApp;
