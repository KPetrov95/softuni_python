    function solve(sentence, word) {
        let censored = '*'.repeat(word.length)
        let sentenceCensored = sentence.replace(word, censored)
        while (sentenceCensored.includes(word)) {
            sentenceCensored = sentenceCensored.replace(word, censored) 
        }
        console.log(sentenceCensored);
    }

solve('A small sentence with some small words', 'small')