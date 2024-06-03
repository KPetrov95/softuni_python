function solve() {
    const departButtonElement = document.getElementById('depart');
    const arriveButtonElement = document.getElementById('arrive');
    const outputElement = document.querySelector('.info');

    const mainURL = 'http://localhost:3030/jsonstore/bus/schedule';

    let nextStop = '';
    let stopId = 'depot';

    function depart() {
        departButtonElement.disabled = 'disabled';
        arriveButtonElement.disabled = '';
        fetch(`${mainURL}/${stopId}`)
        .then(response => response.json())
        .then(busStopData => {
            nextStop = busStopData.name;
            stopId = busStopData.next;
            outputElement.textContent = `Next stop ${nextStop}`
        })
        .catch(err => {
            departButtonElement.disabled = 'disabled';
            arriveButtonElement.disabled = 'disabled';
        })
    }

    async function arrive() {
        try{
            departButtonElement.disabled = '';
            arriveButtonElement.disabled = 'disabled';
            outputElement.textContent = `Arriving at ${nextStop}`
        }
        catch {
            departButtonElement.disabled = 'disabled';
            arriveButtonElement.disabled = 'disabled';
        }
        
    }

    return {
        depart,
        arrive
    };
}

let result = solve();