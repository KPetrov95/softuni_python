function solve(numbers) {
    let result = [];
    const SortedNumbers = numbers.sort((a, b) => (a - b)) ;
    while(SortedNumbers.length > 0) {
        highestNum = SortedNumbers.shift();
        lowestNum = SortedNumbers.pop();
        result.push(highestNum)
        if (lowestNum) {
            result.push(lowestNum)
        }
    }
    return result
}

console.log(solve([1, 65, 3, 52, 48, 63, 31, -3, 18, 56, -8]))