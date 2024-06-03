function solve(a, b, operation) {

    const operations = {
        multiply: (a, b) => a * b,
        divide: (a, b) => a / b,
        subtract: (a, b) => a - b,
        add: (a, b) => a + b,
    }

    result = operations[operation](a, b)
    console.log(result)
}

solve(1, 2, 'multiply')