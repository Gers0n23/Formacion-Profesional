document.addEventListener('DOMContentLoaded', (event) => {
    // Funcion para abrir un modal
    function openModal(modal) {
        modal.style.display = "block";
    }

    // Funcion para cerrar un modal
    function closeModal(modal) {
        modal.style.display = "none";
    }

    // Funcion para cerrar un modal al hacer click fuera de el
    function setupOutsideClick(modal) {
        window.onclick = function(event) {
            if (event.target == modal) {
                closeModal(modal);
            }
        }
    }

    // Funcion para actualizar el modal
    var loginModal = document.getElementById("loginModal");
    var loginBtn = document.getElementById("loginBtn");
    var loginClose = loginModal.getElementsByClassName("close")[0];
    var loginText = document.getElementById("loginText");
    var loginImg = document.getElementById("loginImg");

    loginBtn.onclick = function() {
        openModal(loginModal);
    }

    loginClose.onclick = function() {
        closeModal(loginModal);
    }

    setupOutsideClick(loginModal);

    var loginForm = document.getElementById("loginForm");
    loginForm.onsubmit = function(event) {
        event.preventDefault();
        var username = document.getElementById("username").value;

        loginText.textContent = username;
        loginImg.src = "assets/people.png";

        closeModal(loginModal);
    }

    // Funcion para actualizar el carrito
    var cartModal = document.getElementById("cartModal");
    var cartBtn = document.getElementById("cartBtn");
    var cartClose = cartModal.getElementsByClassName("close")[0];

    cartBtn.onclick = function() {
        openModal(cartModal);
        updateCart();
    }

    cartClose.onclick = function() {
        closeModal(cartModal);
    }

    setupOutsideClick(cartModal);
});
