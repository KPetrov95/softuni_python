function solve(n, array) {
    let newArray = [];
    for (let i=n-1; i>=0; i--) {
        newArray.push(array[i])
    }
    let result = newArray.join(' ')
    console.log(result)
}

solve(3, [10, 20, 30, 40, 50])