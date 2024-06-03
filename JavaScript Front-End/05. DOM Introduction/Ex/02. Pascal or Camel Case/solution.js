function solve() {
  
  textElement = document.querySelector('#text').value;
  conventionElement = document.querySelector('#naming-convention').value;
  resultElement = document.querySelector('#result')

  function pascalCase(text) {
    return text
      .toLowerCase()
      .split(' ')  
      .map(word => word.charAt(0).toUpperCase() + word.slice(1))
      .join('')
  }

  function camelCase(text) {
    return pascalCase(text).charAt(0).toLowerCase() + text.slice(1);
  }

  const convertor = {
    'Pascal Case' : pascalCase,
    'Camel Case' : (text) => pascalCase(text).charAt(0).toLowerCase() + pascalCase(text).slice(1), 
  }
  
  if (convertor[conventionElement]) {
  resultElement.textContent = convertor[conventionElement](textElement);
  }else {
    resultElement.textContent = 'Error!';
  }
}
