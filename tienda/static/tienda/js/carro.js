document.addEventListener("DOMContentLoaded", function() {
    console.log('Carro.js cargado');

    let carrito = [];
    let cuerpo = document.querySelector(".bolsa table tbody");
    let precio = 0;
    let cuenta = document.querySelector(".bolsa .cuenta");
    let total = document.getElementById("precio5");

    function anadir(name, price, url) {
        carrito.push({ name: name, price: price, url: url });
        localStorage.setItem("articulos", JSON.stringify(carrito));
        cuenta.textContent = carrito.length;

        let newPrice = parseFloat(price.replace(/[^0-9.-]+/g, ""));
        if (!isNaN(newPrice)) {
            precio += newPrice;
            total.textContent = precio.toFixed(2);
            localStorage.setItem("precio", precio.toFixed(2));
        } else {
            console.error(`El precio "${price}" no es válido`);
        }
        actualizar();
    }

    function actualizar() {
        cuerpo.innerHTML = "";
        carrito.forEach(function(item, index) {
            let fila = document.createElement("tr");
            let imagen = document.createElement("img");
            imagen.src = item.url;

            let tdImagen = document.createElement("td");
            tdImagen.appendChild(imagen);
            fila.appendChild(tdImagen);

            fila.innerHTML += `
                <td>${item.name}</td>
                <td>${item.price}</td>
                <td><a href="#" onclick="return eliminar(${index});">X</a></td>
            `;

            cuerpo.appendChild(fila);
        });
    }

    window.eliminar = function(index) {
        let position = carrito[index];
        carrito.splice(index, 1);

        let delPrice = parseFloat(position.price.replace(/[^0-9.-]+/g, ""));
        if (!isNaN(delPrice)) {
            precio -= delPrice;
            if (precio < 0) precio = 0;
            total.textContent = precio.toFixed(2);
            localStorage.setItem("precio", precio.toFixed(2));
        } else {
            console.error(`El precio "${position.price}" no es válido`);
        }

        cuenta.textContent = carrito.length;
        localStorage.setItem("articulos", JSON.stringify(carrito));
        actualizar();

        return false;
    }

    function cargar() {
        let itemlocal = localStorage.getItem("articulos");
        let preciolocal = localStorage.getItem("precio");

        if (itemlocal) {
            carrito = JSON.parse(itemlocal);
            precio = parseFloat(preciolocal) || 0;
            total.textContent = precio.toFixed(2);
            actualizar();
        }
    }

    document.querySelectorAll(".update-cart").forEach(button => {
        button.addEventListener("click", function() {
            const productId = this.getAttribute("data-product");
            const card = document.querySelector(`.card[data-product-id="${productId}"]`);

            if (!card) {
                console.error(`No se encontró la tarjeta del producto con ID: ${productId}`);
                return;
            }

            const name = card.querySelector("h3").textContent;
            const price = card.querySelector("p").textContent;
            const url = card.querySelector(".imagen img").getAttribute("src");

            if (!name || !price || !url) {
                console.error(`No se pudieron obtener los datos del producto: ${productId}`);
                return;
            }

            anadir(name, price, url);

            const modalId = `#exampleModal${productId}`;
            console.log(`ID del modal: ${modalId}`);
            const modalElement = document.querySelector(modalId);
            if (modalElement) {
                const modal = bootstrap.Modal.getInstance(modalElement);
                if (modal) {
                    modal.hide();
                } else {
                    console.error(`No se encontró el modal con ID: ${modalId}`);
                }
            } else {
                console.error(`No se encontró el elemento del modal con ID: ${modalId}`);
            }
        });
    });

    const bolsa = document.querySelector(".bolsa");
    const carritoElement = document.querySelector(".carrito");

    bolsa.addEventListener("click", function() {
        if (carritoElement.style.display === "none" || carritoElement.style.display === "") {
            carritoElement.style.display = "block";
        } else {
            carritoElement.style.display = "none";
        }
    });

    document.addEventListener('show.bs.modal', function() {
        carritoElement.style.position = 'absolute'; // Asegúrate de que el carrito esté en la posición correcta
    });

    document.addEventListener('hide.bs.modal', function() {
        carritoElement.style.position = 'absolute'; // Restablece la posición si es necesario
    });

    cargar();
});
