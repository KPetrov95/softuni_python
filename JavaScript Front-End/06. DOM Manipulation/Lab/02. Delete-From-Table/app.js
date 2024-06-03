function deleteByEmail() {
    const tableRowElements = document.querySelectorAll('tbody tr');
    const inputElement = document.querySelector('input[type=text]');
    const outputElement = document.querySelector('div#result');

    const resultElement = Array
        .from(tableRowElements)
        .find(Element => Element.children[1].textContent.includes(inputElement.value));

    if(resultElement){
        resultElement.remove();
        outputElement.textContent = 'Deleted';
    }else {
        outputElement.textContent = 'Not found.'
    }
}