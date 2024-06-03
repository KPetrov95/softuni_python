function subtract() {
    const numOne = Number(document.querySelector('#firstNumber').value);
    const numTwo = Number(document.querySelector('#secondNumber').value);
    let resultElement = document.querySelector('#result');
    const result = numOne - numTwo;
    resultElement.textContent = result;
}