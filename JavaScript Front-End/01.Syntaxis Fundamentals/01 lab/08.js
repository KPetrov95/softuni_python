function solve(number) {
    let result;
    inputType = typeof(number)
    if (inputType === 'number') {
        result = (Math.pow(number, 2) * Math.PI).toFixed(2)
    }
    else {
        result = `We can not calculate the circle area, because we receive a ${inputType}.`
    }
    console.log(result)
}

solve(5)