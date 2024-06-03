function focused() {
    const inputElements = document.querySelectorAll('input[type=text]');

    Array.from(inputElements).forEach(inputEl => {
        inputEl.addEventListener('focus', () => inputEl.parentElement.classList.add('focused'))
    })

    Array.from(inputElements).forEach(inputEl => {
        inputEl.addEventListener('blur', () => inputEl.parentElement.classList.remove('focused'))
    })
}