// Función para eliminar un producto
document.querySelectorAll('.delete-button').forEach(button => {
    button.addEventListener('click', () => {
        button.parentElement.remove();
        updateTotal();
    });
});

// Función para aumentar la cantidad de unidades
document.querySelectorAll('.increment-button').forEach(button => {
    button.addEventListener('click', () => {
        const quantityElement = button.nextElementSibling;
        quantityElement.textContent = parseInt(quantityElement.textContent) + 1;
        updateTotal();
    });
});

// Función para disminuir la cantidad de unidades
document.querySelectorAll('.decrement-button').forEach(button => {
    button.addEventListener('click', () => {
        const quantityElement = button.previousElementSibling;
        const quantity = parseInt(quantityElement.textContent);
        if (quantity > 1) {
            quantityElement.textContent = quantity - 1;
            updateTotal();
        }
    });
});

// Función para actualizar el total
function updateTotal() {
    const prices = Array.from(document.querySelectorAll('.product p')).map(p => parseFloat(p.textContent.replace('Precio: $', '')));
    const quantities = Array.from(document.querySelectorAll('.quantity')).map(q => parseInt(q.textContent));
    const total = prices.reduce((acc, price, index) => acc + price * quantities[index], 0).toFixed(3);
    document.querySelector('.total p').textContent = `Total: $${total}`;
}