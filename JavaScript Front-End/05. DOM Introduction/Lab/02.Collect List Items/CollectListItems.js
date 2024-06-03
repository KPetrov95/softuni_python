function extractText() {
    const inputElements = document.getElementsByTagName('li');
    const placeElement = document.getElementById('result');
    for (element of inputElements) {
        placeElement.value += element.textContent +'\n';
    }
}