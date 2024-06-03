function solve() {
  inputElement = document.querySelector('#exercise textarea:first-of-type');
  outputElement = document.querySelector('#exercise textarea:last-of-type');
  generateButtonElement = document.querySelector('#exercise button:first-of-type');
  buyButtonElement = document.querySelector('#exercise button:last-of-type');
  tBodyElement = document.querySelector('.table tbody')

  generateButtonElement.addEventListener('click', () => {
      const furnitures = JSON.parse(inputElement.value);
      for (const furniture of furnitures) {
          const imgElement = document.createElement('img');
          imgElement.src = furniture.img;
          const imgTdElement = document.createElement('td');
          imgTdElement.appendChild(imgElement);

          const namePElement = document.createElement('p');
          namePElement.textContent = furniture.name;
          const nameTdElement = document.createElement('td');
          nameTdElement.appendChild(namePElement);

          const pricePElement = document.createElement('p');
          pricePElement.textContent = furniture.price;
          const priceTdElement = document.createElement('td');
          priceTdElement.appendChild(pricePElement);

          const decFactorPElement = document.createElement('p');
          decFactorPElement.textContent = furniture.decFactor;
          const decFactorTdElement = document.createElement('td');
          decFactorTdElement.appendChild(decFactorPElement);

          const markedInputElement = document.createElement('input')
          markedInputElement.type = 'checkbox'
          const markedTdElement = document.createElement('td')
          markedTdElement.appendChild(markedInputElement)

          trElement = document.createElement('tr');
          trElement.appendChild(imgTdElement)
          trElement.appendChild(nameTdElement)
          trElement.appendChild(priceTdElement)
          trElement.appendChild(decFactorTdElement)
          trElement.appendChild(markedTdElement)

          tBodyElement.appendChild(trElement);
          
      }
  })

  buyButtonElement.addEventListener('click', () => {
      let totalPrice = 0;
      let names = [];
      let totalDecFactor = 0;
      
      Array.from(tBodyElement.children)
          .forEach(trElement => {
              const markedElement = trElement.querySelector('input[type=checkbox]');
              if (!markedElement.checked) {
                  return;
              }
              names.push(trElement.children[1].textContent);
              totalPrice += Number(trElement.children[2].textContent);
              totalDecFactor += Number(trElement.children[3].textContent);
          } )
      outputElement.textContent += `Bought furniture: ${names.join(', ')}\n`
      outputElement.textContent += `Total price: ${totalPrice.toFixed(2)}\n`
      outputElement.textContent += `Average decoration factor: ${totalDecFactor / names.length}`
  })
}