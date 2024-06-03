function solve(sentence, word) {
    let array = sentence.split(' ');
    let count = 0;
    array.forEach((element) => {
        if (element == word) {
            count += 1
        }
    });
    console.log(count);
}
solve('This is a word and it also is a sentence',
'is'
)