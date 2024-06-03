function attachEvents() {
    const mainUrl = 'http://localhost:3030/jsonstore/messenger';

    const submitButtonElement = document.getElementById('submit');
    const refreshButtonElement = document.getElementById('refresh');

    const authorElement = document.querySelector('input[name=author]');
    const contentElement = document.querySelector('input[name=content]');

    const msgArea = document.querySelector('#messages');

    refreshButtonElement.addEventListener('click', () => {
        msgArea.textContent = '';
        const msgArray = [];
        fetch(mainUrl)
        .then(res => res.json())
        .then(data => {for (msg of Object.values(data)) {
            msgArray.push(`${msg.author}: ${msg.content}`)
            msgArea.textContent = msgArray.join('\n')
        }
        })
    })

    submitButtonElement.addEventListener('click', () => {
        const author = authorElement.value;
        const content = contentElement.value;

        const message = {
            author,
            content,
        }

        fetch(mainUrl, {
            method: 'POST',
            body: JSON.stringify(message)
        })

        contentElement.value = '';
        authorElement.value = '';
    })

}

attachEvents();