function solve(number) {
    const result = printSums(getSums(getArray(number)))
    return result

    function getArray(number) {
        array = number.toString()
        .split('')
        return array
    }

    function getSums(arrayOfNums) {
        let oddSum = 0;
        let evenSum = 0;
        for (let i = 0; i < arrayOfNums.length; i++) {
            if (arrayOfNums[i] % 2 == 0) {
                evenSum += Number(arrayOfNums[i]);
            }else {
                oddSum += Number(arrayOfNums[i]);
            }
        }
        return [oddSum, evenSum]
    }

    function printSums(arrayOfSums) {
        return `Odd sum = ${arrayOfSums[0]}, Even sum = ${arrayOfSums[1]}`
    }
}

console.log(solve(1000435));