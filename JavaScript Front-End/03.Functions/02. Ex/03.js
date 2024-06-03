function solve(a, b) {
    const [startChar, endChar] = sortCharacters(a, b);
    let result = printChars(getBetween(startChar, endChar));
    return result

    function sortCharacters(...chars) {
        return chars.sort()
    }

    function getBetween(startChar, endChar) {
        let start = startChar.charCodeAt(0);
        let end = endChar.charCodeAt(0);
        let charsBetween = [];
        for (let i = start + 1; i < end; i++) {
            charsBetween.push(String.fromCharCode(i))
        }
        return charsBetween
    }

    function printChars(chars) {
        return chars.join(' ')
    }
}

console.log(solve('C',
'#'
));