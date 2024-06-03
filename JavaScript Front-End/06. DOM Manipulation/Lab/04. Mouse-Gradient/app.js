function attachGradientEvents() {
    const gradientElement = document.getElementById('gradient')
    const resultElement = document.getElementById('result')

    gradientElement.addEventListener('mousemove', (event) => {
        const gradientWidth = gradientElement.clientWidth;
        const currentWidth = event.offsetX;
        const result = Math.floor((currentWidth / gradientWidth) * 100);
        resultElement.textContent = `${result}%`;
    })
}