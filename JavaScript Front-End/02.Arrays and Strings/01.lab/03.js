function solve(numbers) {
    let oddSum = 0;
    let evenSum = 0;
    numbers.forEach((element) => {
        if (element % 2 == 0) {
            evenSum += element;
        }
        else {
            oddSum += element
        }
    });
    console.log(evenSum - oddSum);
}

solve([3,5,7,9])