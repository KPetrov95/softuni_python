function addItem() {
    const listElement = document.getElementById('items')
    const newElement = document.createElement('li')
    const inputElement = document.getElementById('newItemText')

    newElement.textContent = inputElement.value;
    listElement.appendChild(newElement);

    // create delete element
    const deleteElement = document.createElement('a');
    deleteElement.textContent = '[Delete]'
    deleteElement.href = '#';

    // create listener and implement function
    deleteElement.addEventListener('click', () => {
        newElement.remove();
    })

    // append delete element to new element
    newElement.appendChild(deleteElement);

    //clear input
    inputElement.value = '';
    
}