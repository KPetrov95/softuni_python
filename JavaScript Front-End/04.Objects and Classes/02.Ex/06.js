function solve(input) {
    keyWords = input
        .shift()
        .split(' ')
        .reduce((result, word) => ({...result, [word] : 0}) ,{});
    
    for (const word of input) {
        if (keyWords.hasOwnProperty(word)) {
            keyWords[word] += 1;
        }
    }

    Object
        .entries(keyWords)
        .sort((a, b) => b[1] - a[1])
        .forEach(([word, occurences]) => console.log(`${word} - ${occurences}`));

}

solve([
    'this sentence', 
    'In', 'this', 'sentence', 'you', 'have', 'to', 'count', 'the', 'occurrences', 'of', 'the', 'words', 'this', 'and', 'sentence', 'because', 'this', 'is', 'your', 'task'
    ]
    )