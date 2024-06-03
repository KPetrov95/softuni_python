function getInfo() {
    const checkButtonElement = document.getElementById('submit');
    const stopNameElement = document.getElementById('stopName');
    const busesUlElement = document.getElementById('buses');
    const inputElement = document.getElementById('stopId');

    const url = 'http://localhost:3030/jsonstore/bus/businfo'
    busesUlElement.textContent = '';
    fetch(`${url}/${inputElement.value}`)
        .then(result => result.json())
        .then(value => {
            stopNameElement.textContent = value.name;
            const buses = value.buses
            const busesFragment = document.createDocumentFragment()
            for (const busId in buses) {
                const busLiElement = document.createElement('li');
                busLiElement.textContent = `Bus ${busId} arrives in ${buses[busId]} minutes`;
                busesFragment.appendChild(busLiElement);
            }
            busesUlElement.appendChild(busesFragment);
        })
        .catch(err => stopNameElement.textContent = 'Error')
    
}