function solve(number) {
    function getDivisors(number) {
        let divisors = [];
        for (let i = number; i >= 0; i-- ) {
            if (number % i == 0) {
                divisors.push(i);
            }
        }
        return divisors
    }
    function getSum(numbers) {
        sum = numbers.reduce((a,b) => a + b, 0)
        return sum
    }

    function isPerfect(number) {
        return number === (getSum(getDivisors(number)) / 2);
    }

    if (isPerfect(number)) {
        return "We have a perfect number!";
    }else {
        return "It's not so perfect."
    }
    
}

console.log(solve(1236498));