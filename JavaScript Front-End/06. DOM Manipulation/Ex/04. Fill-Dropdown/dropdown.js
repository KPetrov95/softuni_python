function addItem() {
    inputTextElement = document.getElementById('newItemText');
    inputValueElement = document.getElementById('newItemValue');
    selectElement = document.getElementById('menu');

    newElement = document.createElement('option');
    newElement.textContent = inputTextElement.value;
    newElement.value = inputValueElement.value;
    selectElement.appendChild(newElement);
    inputTextElement.value = '';
    inputValueElement.value = '';
}