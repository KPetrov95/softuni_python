function solve(array, n) {
    for (let i = 1; i <= n; i++) {
        let numToShift = array.shift();
        array.push(numToShift)
    }
    console.log(array.join(' '));
}

solve([32, 21, 61, 1], 4)