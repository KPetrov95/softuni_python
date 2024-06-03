function solve(number, power) {
    let result = 1
    for(let i = 0; i < power; i++) {
        result *= number
    }
    return result
}

console.log(solve(2, 8));