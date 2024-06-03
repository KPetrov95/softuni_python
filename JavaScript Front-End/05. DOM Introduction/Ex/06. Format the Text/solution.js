function solve() {
  const inputElement = document.getElementById('input');
  const outputElement = document.getElementById('output');

  const text = inputElement.value;

  const result = text
      .split('.')
      .filter(sentence => !!sentence)
      .reduce((result, sentence, i) => {
          const resultIndex = Math.floor(i / 3);
          if (!result[resultIndex]) {
              result[resultIndex] = []
          }

          result[resultIndex].push(sentence.trim());

          return result;
      }, [])
      .map(sentences => `<p>${sentences.join('. ')}.</p>`)
      .join('\n');

  outputElement.innerHTML = result;
}