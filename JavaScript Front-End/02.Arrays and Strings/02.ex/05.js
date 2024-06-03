function solve(keyWords = '', sentence) {
    let keyArray = keyWords.split(', ')
    let sentenceArray = sentence.split(' ')
    for (let i = 0; i < sentenceArray.length; i++) {
        if (sentenceArray[i].includes('*')) {
            let word = sentenceArray[i]
            const neededWord = keyArray.find(w => w.length === word.length);
            sentence = sentence.replace(word, neededWord)
        }
    }
    console.log(sentence);
}

solve('great',
'softuni is ***** place for learning new programming languages'
)