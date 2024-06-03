function solve(arrayNums) {
    arrayNums.forEach(printPalndrome)

    function checkPalindrome(number) {
        originalNumber = number.toString();
        reversedNumber = originalNumber.split('').reverse().join('');

        return originalNumber === reversedNumber;
    }

    function printPalndrome(number) {
        console.log(checkPalindrome(number));
    }
}

solve([121])