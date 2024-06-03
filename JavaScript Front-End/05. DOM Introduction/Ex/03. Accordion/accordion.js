function toggle() {
    const buttonElement = document.querySelector('.head span.button');
    const textElement = document.querySelector('#extra');
 
    let buttonText = buttonElement.textContent
 
    if (buttonText === 'More') {
         buttonElement.textContent = 'Less';
         textElement.style.display = 'block';
    }else {
         buttonElement.textContent = 'More';
         textElement.style.display = 'none';
    }
 }