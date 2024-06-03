function solve(a, b, c) {
    const sum = (a, b) => a + b;
    const subtract = (a, b) => a - b;
    return subtract(sum(a, b), c)
}

console.log(solve(23,
    6,
    10
    ));