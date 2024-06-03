function addItem() {
    const listElement = document.getElementById('items')
    const newElement = document.createElement('li')
    const inputElement = document.getElementById('newItemText')
    newElement.textContent = inputElement.value;
    listElement.appendChild(newElement);
}