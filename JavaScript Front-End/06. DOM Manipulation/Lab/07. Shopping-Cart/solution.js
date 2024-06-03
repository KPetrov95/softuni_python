function solve() {
   
   const addButtonElements = document.querySelectorAll('button.add-product');
   const checkoutButtonElement = document.querySelector('button.checkout');
   const textArea = document.querySelector('textarea')

   let totalPrice = 0;
   let uniqueElements = new Set();

   for (const buttonElement of addButtonElements) {
      const productElement = buttonElement.parentElement.parentElement;

      buttonElement.addEventListener('click', () => {
         const price = Number(productElement.querySelector('.product-line-price').textContent);
         const title = productElement.querySelector('.product-title').textContent;

         totalPrice += price;
         uniqueElements.add(title);
         textArea.value += `Added ${title} for ${price.toFixed(2)} to the cart.\n`;
      })
   }

   checkoutButtonElement.addEventListener('click', () => {
      Array.from(addButtonElements).forEach(buttonElement => {
         buttonElement.setAttribute('disabled', 'disabled');
   })
   checkoutButtonElement.setAttribute('disabled', 'disabled');
   result = Array.from(uniqueElements).join(', ');
   textArea.value += `You bought ${result} for ${totalPrice.toFixed(2)}.`
   })
}