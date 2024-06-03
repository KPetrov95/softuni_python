function attachEventsListeners() {
    secondsButtonElement = document.getElementById('secondsBtn')
    minutesButtonElement = document.getElementById('minutesBtn')
    hoursButtonElement = document.getElementById('hoursBtn')
    daysButtonElement = document.getElementById('daysBtn')

    secondsInputElement = document.getElementById('seconds')
    minutesInputElement = document.getElementById('minutes')
    hoursInputElement = document.getElementById('hours')
    daysInputElement = document.getElementById('days')

    
    daysButtonElement.addEventListener('click', () => {
        days = daysInputElement.value;
        hoursInputElement.value = days * 24;
        minutesInputElement.value = days * 24 * 60;
        secondsInputElement.value = days * 24 * 60 * 60;
    })

    hoursButtonElement.addEventListener('click', () => {
        const hours = hoursInputElement.value;
        daysInputElement.value = hours / 24;
        minutesInputElement.value = hours * 60;
        secondsInputElement.value = hours * 60 * 60;
     });

     minutesButtonElement.addEventListener('click', () => {
        const minutes = minutesInputElement.value
        daysInputElement.value = minutes / 60 / 24;
        hoursInputElement.value = minutes / 60;
        secondsInputElement.value = minutes * 60;
     })
    
     secondsButtonElement.addEventListener('click', () => {
        const seconds = secondsInputElement.value
        daysInputElement.value = seconds / 24 / 60 / 60;
        hoursInputElement.value = seconds / 60 / 60;
        minutesInputElement.value = seconds / 60;
     })
}