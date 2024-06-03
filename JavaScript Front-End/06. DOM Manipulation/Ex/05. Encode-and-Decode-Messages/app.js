function encodeAndDecodeMessages() {
    //get elements  
    inputFieldElement = document.querySelector('div:nth-child(1) textarea:nth-child(2)');
    outputFieldElement = document.querySelector('div:nth-child(2) textarea:nth-child(2)');
    encodeButtonElement = document.querySelector('div:nth-child(1) button:nth-child(3)');
    decodeButtonElement = document.querySelector('div:nth-child(2) button:nth-child(3)');

    //encode, transfer to other field and clear input

    encodeButtonElement.addEventListener('click', () => {
       const msg = inputFieldElement.value;
       let codedmsg = '';

       for (char of msg) {
        const asciiValue= char.charCodeAt() + 1;
        codedmsg += String.fromCharCode(asciiValue)
       }
       outputFieldElement.value = codedmsg;
       inputFieldElement.value = '';
    })

    //display decoded msg

    decodeButtonElement.addEventListener('click', () => {
        const encodedmsg = outputFieldElement.value
        let decodedmsg = '';
        for (const char of encodedmsg) {
            const asciiValue = char.charCodeAt() - 1;
            decodedmsg += String.fromCharCode(asciiValue);
        }
        outputFieldElement.value = decodedmsg
    })
}