function solve(num) {
    let numAsStr = num.toString();
    let sum = 0;
    let same = true;
    for(let i = 0; i < numAsStr.length; i++) {
        if (numAsStr[i] != numAsStr[0]) {
            same = false;
        }
        sum += Number(numAsStr[i])
    }
    console.log(same)
    console.log(sum)
}

solve(2222222)