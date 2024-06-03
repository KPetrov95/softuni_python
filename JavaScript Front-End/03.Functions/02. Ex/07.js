function solve(num) {
    const createRow = (number) => new Array(number).fill(number).join(' ')

    for (let i = 0; i < num; i++) {
        console.log(createRow(num));
    }
}

solve(7)