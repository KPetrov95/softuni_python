function solve(input) {
    const result = {};
    let words = input.split(' ');
    for (const word of words) {
        if (!result[word.toLowerCase()]) {
            result[word.toLowerCase()] = 0;
        }
        result[word.toLowerCase()] += 1;
    }
    const final = Object
        .entries(result)
        .filter(([a, b]) => b % 2 !== 0)
        .map(([word, count]) => word)
        .join(' ')
    console.log(final);
}

solve('Java C# Php PHP Java PhP 3 C# 3 1 5 C#')