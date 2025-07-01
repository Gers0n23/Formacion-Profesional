document.addEventListener('DOMContentLoaded', (event) => {
    // Carrito de compras
    let cart = [];

    // Función para actualizar el carrito en la página
    
    function updateCart() {
        const cartItems = document.getElementById('cartItems');
        const totalPriceElement = document.getElementById('totalPrice');
        cartItems.innerHTML = '';
        let totalPrice = 0;
        const cartQuantityElement = document.querySelector('.hijo.p');
        cartQuantityElement.textContent = cart.length;

        const cartContainer = document.querySelector('.hijo');
        if (cart.length < 1) {
            cartContainer.style.backgroundColor = 'transparent';
            cartContainer.style.color = 'black';
        } else {
            // Restaurar el color de fondo y el color de texto 
            cartContainer.style.backgroundColor = ''; 
            cartContainer.style.color = ''; 
        }

        cart.forEach((item, index) => {
            const cartItem = document.createElement('div');
            cartItem.classList.add('cart-item');

            cartItem.innerHTML = `
                <img src="${item.image}" alt="${item.name}" width="50" height="50">
                <span>${item.name}</span>
                <span>Cantidad: ${item.quantity}</span>
                <span>Precio: $${(item.price * item.quantity)}</span>
                <button class="decrease-btn" data-index="${index}">-</button>
                <button class="increase-btn" data-index="${index}">+</button>
                <button class="remove-btn" data-index="${index}">Eliminar</button>
            `;

            cartItems.appendChild(cartItem);
            totalPrice += item.price * item.quantity;
        });

        totalPriceElement.textContent = `Total: $${totalPrice}`;

        // Event listeners para los botones de incrementar, disminuir y eliminar productos del carrito
        document.querySelectorAll('.increase-btn').forEach(button => {
            button.addEventListener('click', (event) => {
                const index = event.target.getAttribute('data-index');
                cart[index].quantity += 1;
                updateCart();
            });
        });

        document.querySelectorAll('.decrease-btn').forEach(button => {
            button.addEventListener('click', (event) => {
                const index = event.target.getAttribute('data-index');
                if (cart[index].quantity > 1) {
                    cart[index].quantity -= 1;
                } else {
                    cart.splice(index, 1);
                }
                updateCart();
            });
        });

        document.querySelectorAll('.remove-btn').forEach(button => {
            button.addEventListener('click', (event) => {
                const index = event.target.getAttribute('data-index');
                cart.splice(index, 1);
                updateCart();
            });
        });
    }

    document.addEventListener('DOMContentLoaded', updateCart);
    updateCart();

    // Función para agregar un producto al carrito
    function addToCart(name, price, image) {
        const existingProductIndex = cart.findIndex(product => product.name === name);
        const productInCatalog = catalogo.find(product => product.nombre === name);
    
        if (productInCatalog.disponibilidad > 0) {
            productInCatalog.disponibilidad -= 1;
    
            if (existingProductIndex !== -1) {
                cart[existingProductIndex].quantity += 1;
            } else {
                cart.push({ name, price, image, quantity: 1 });
            }
    
            updateCart();
            updateCatalog();
            updateProductAvailability(producto);
        } else {
            console.log('Producto no disponible');
        }
    }

    function updateCatalog() {
        catalogo.forEach(producto => {
            const productElement = document.getElementById(producto.nombre);
            if (productElement) {
                const availabilityElement = productElement.querySelector('.disponibilidad');
                if (availabilityElement) {
                    availabilityElement.textContent = `Disponibilidad: ${producto.disponibilidad}`;
                }
            }
        });
    }

    function updateProductAvailability(producto) {
        const productCard = document.getElementById(producto.nombre);
        if (productCard) {
            const availabilityElement = productCard.querySelector('p:nth-child(4)');
            availabilityElement.textContent = `Stock: ${producto.disponibilidad} un`;
        }
    }

    // Event listener para los botones "Agregar al carrito"
    const addToCartButtons = document.querySelectorAll('.add-to-cart-btn');
    addToCartButtons.forEach(button => {
        button.addEventListener('click', (event) => {
            const productCard = event.target.closest('.product-card');
            const name = productCard.querySelector('h3').textContent;
            const price = parseFloat(productCard.querySelector('p').textContent.replace('Precio: $', ''));
            const image = productCard.querySelector('img').src;

            addToCart(name, price, image);
        });
    });

    // Función para finalizar la compra
    function checkout() {
        // Guardar los detalles de la compra, dirección y datos del cliente inventados
        const orderDetails = {
            items: cart,
            shippingAddress: "Avenida siempre viva 123, Springfield, USA",
            customerName: "Homero Simpson",
            // Agrega más detalles del cliente según sea necesario
        };

        // Guardar los detalles de la compra en el almacenamiento local
        localStorage.setItem('orderDetails', JSON.stringify(orderDetails)); 

        // Redirigir a la página de confirmación de compra después de guardar los datos
        window.location.href = 'confirmacion_compra.html'; 
    }

    // Event listener para el botón "Finalizar Compra"
    const checkoutBtn = document.getElementById('checkoutBtn');
    checkoutBtn.addEventListener('click', checkout);
});

function checkoutback() {

    // Redirigir a la página de confirmación de compra después de guardar los datos
    window.location.href = 'index.html';
    const backcheckoutBtn = document.getElementById('checkoutBtn');
    backcheckoutBtn.addEventListener('click', checkoutback); 
}

document.addEventListener('DOMContentLoaded', function() {

    let totalPrice = 0;

    // Recuperar los detalles del carrito del almacenamiento local
    const orderDetailsString = localStorage.getItem('orderDetails');
    const orderDetails = JSON.parse(orderDetailsString);

    // Verificar si se recuperaron correctamente los detalles del carrito
    if (orderDetails) {
        // Mostrar los detalles del carrito en la página
        const orderSummary = document.getElementById('orderSummary');
        const customerName = document.getElementById('customerName');
        const customerAddress = document.getElementById('customerAddress');
        const cardNumber = document.getElementById('cardNumber');
        const expiryDate = document.getElementById('expiryDate');
        const cvv = document.getElementById('cvv');

        // Mostrar los detalles del cliente
        customerName.value = orderDetails.customerName;
        customerAddress.value = orderDetails.shippingAddress;
        cardNumber.value = "1264-5678-1234-5678";
        expiryDate.value = "12/23";
        cvv.value = "123";

        // Mostrar el resumen de la compra
        const cartItems = orderDetails.items;
        cartItems.forEach(item => {
            const cartItem = document.createElement('div');
            cartItem.classList.add('cart-item');
            cartItem.innerHTML = `
                <img src="${item.image}" alt="${item.name}" width="50" height="50">
                <span>${item.name}</span>
                <span>Cantidad: ${item.quantity}</span>
                <span>Precio: $${(item.price * item.quantity)}</span>
            `;
            orderSummary.appendChild(cartItem);
            totalPrice += item.price * item.quantity;
        });
    } else {
        console.error('No se encontraron detalles del carrito en el almacenamiento local');
    }
    const totalPriceElement = document.getElementById('totalPrice');
    totalPriceElement.textContent = `Total: $${totalPrice}`;
    
});

