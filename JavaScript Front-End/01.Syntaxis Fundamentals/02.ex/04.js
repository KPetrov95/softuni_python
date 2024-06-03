function solve(startNumber, endNumber) {
    let numbers = '';
    let sum = 0;
    for (let i=startNumber; i<=endNumber; i++) {
        sum += i;
        numbers += `${i} `;
    }
    console.log(numbers)
    console.log(`Sum: ${sum}`)
}

solve(0, 26)