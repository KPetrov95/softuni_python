function solve(a, b) {
    const result = calcFactorial(a) / calcFactorial(b)
    return result.toFixed(2)
    function calcFactorial(number) {
        if (number <= 1) {
            return 1;
        }
        return number * calcFactorial(number - 1);
    }
}

console.log(solve(5, 2));