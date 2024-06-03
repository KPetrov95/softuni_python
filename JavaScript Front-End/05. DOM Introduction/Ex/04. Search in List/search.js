function search() {
   const townlistElement = document.getElementById('towns');
   const resultElement = document.getElementById('result');
   const searchText = document.getElementById('searchText').value;
   
   
   const townElements = Array.from(townlistElement.children);  
   let matches = 0;

   for (let town of townElements) {
      if (town.textContent.toLowerCase().includes(searchText.toLowerCase())) {
         town.style.textDecoration = 'underline';
         town.style.fontWeight = 'bold';
         matches++;
      }
   }
   resultElement.textContent = `${matches} matches found`;
}