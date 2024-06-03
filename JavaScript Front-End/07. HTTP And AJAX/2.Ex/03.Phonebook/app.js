function attachEvents() {
    // get all elements
    const mainUrl = 'http://localhost:3030/jsonstore/phonebook' 

    const loadButtonElement = document.getElementById('btnLoad');
    const createButtonElement = document.getElementById('btnCreate');
    const personInputElement = document.getElementById('person');
    const phoneInputElement = document.getElementById('phone');
    const phonebookUlElement = document.getElementById('phonebook');

    loadButtonElement.addEventListener('click', DisplayPhonesEvent)
    createButtonElement.addEventListener('click', CreatePhoneEntry)

    async function DisplayPhonesEvent() {
        let response = await fetch(mainUrl);
        const phonesObjs = await response.json();
        
        for(let phone of Object.entries(phonesObjs)) {
            const deleteButton = document.createElement('button');
            deleteButton.textContent = 'Delete';
            const liElement = document.createElement('li');
            liElement.textContent = `${phone[1].person}: ${phone[1].phone}`;
            liElement.appendChild(deleteButton)
            phonebookUlElement.appendChild(liElement);

            deleteButton.addEventListener('click', () => {
                fetch(`${mainUrl}/${phone[1]._id}`, {
                    method: 'DELETE',
                })
                .then(() => {
                    liElement.remove()
                })
            })
        }
    }

    async function CreatePhoneEntry() {
        const phone = phoneInputElement.value;
        const person = personInputElement.value;

        fetch(mainUrl, {
            method: 'POST',
            body: JSON.stringify({
                person,
                phone,
            })
        })
        DisplayPhonesEvent()
    }
}

attachEvents();