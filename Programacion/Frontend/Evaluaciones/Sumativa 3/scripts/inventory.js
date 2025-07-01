// Script que se encarga de mostrar los productos en el catálogo.

document.addEventListener('DOMContentLoaded', function() {
    const productContainer = document.querySelector('.product-container');

    catalogo.forEach(producto => {
        const productCard = document.createElement('div');
        productCard.classList.add('product-card');
        productCard.id = producto.nombre;

        productCard.innerHTML = `
            <img src="assets/${producto.imagen}" alt="${producto.nombre}" width="230" height="80">
            <h3>${producto.nombre}</h3>
            <p>Precio: $${producto.precio}</p>
            <p>Stock: ${producto.disponibilidad} un</p>
            <button class="add-to-cart-btn">Agregar al carrito</button ali>
        `;

        productContainer.appendChild(productCard);
    });
});