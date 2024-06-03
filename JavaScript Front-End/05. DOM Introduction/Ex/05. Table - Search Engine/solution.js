function solve() {
   document.querySelector('#searchBtn').addEventListener('click', onClick);

   function onClick() {
      const textElement = document.getElementById('searchField');
      const searchText = document.getElementById('searchField').value;
      const tRowElements = document.querySelectorAll('table.container tbody tr');

      for(const trElement of tRowElements) {
         const dataElements = trElement.querySelectorAll('td')
         trElement.classList.remove('select');
         for (const tdElement of dataElements) {
            if (tdElement.textContent.toLowerCase().includes(searchText.toLowerCase())){
               trElement.classList.add('select');
               break
            }

         }
      }
      textElement.value = '';
   }
}