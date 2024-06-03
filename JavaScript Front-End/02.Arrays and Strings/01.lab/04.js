function solve(string, start, count) {
    let substring = '';
    for (let i = start; i <= count; i++) {
        substring += string[i]
    }
    console.log(substring);
}

solve('ASentence', 1, 8)