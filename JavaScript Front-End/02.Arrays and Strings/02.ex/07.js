function solve(keyWord, sentence) {
    const arraySentence = sentence.split(' ');
    for (const word of arraySentence) {
        if (word.toLowerCase() === keyWord.toLowerCase()) {
            return keyWord
        }
    }
    return `${keyWord} not found!`
}

console.log(solve('java',
'JavaScript is the best programming language'
));