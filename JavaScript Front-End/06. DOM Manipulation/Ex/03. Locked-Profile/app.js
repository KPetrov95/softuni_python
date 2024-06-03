function lockedProfile() {
    profileElements = document.querySelectorAll('.profile')

    for (const profile of profileElements) {
        const radioButtonElement = profile.querySelector('input[type=radio][value=lock]');
        const infoButtonElement = profile.querySelector('button');
        const infoElement = infoButtonElement.previousElementSibling;

        infoButtonElement.addEventListener('click', () => {
            if (radioButtonElement.checked) {
                return;
            }
            if (infoButtonElement.textContent === 'Show more') {
                infoElement.style.display = 'block';
                infoButtonElement.textContent = 'Hide it';
            }else {
                infoElement.style.display = 'none';
                infoButtonElement.textContent = 'Show more';
            }
        })
        
    }
}