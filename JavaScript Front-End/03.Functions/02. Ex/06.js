function solve(password) {
    let isValid = true

    function isNumber(char) {
        return typeof char === 'integer';
    }

    function isValidLength(password) {
        return (password.length >= 6 && password.length <= 10);
    }

    function isAlphaNumerical(password) {
        return  /^[a-zA-Z0-9]+$/.test(password);
    }   

    function isStrong(password) {
        nums = password.split('').filter(char => Number.isInteger(Number(char)));
        return nums.length >= 2;
    }

    if (!isValidLength(password)) {
        isValid = false;
        console.log("Password must be between 6 and 10 characters");
    }

    if (!isAlphaNumerical(password)) {
        isValid = false;
        console.log("Password must consist only of letters and digits");
    }

    if (!isStrong(password)) {
        isValid = false;
        console.log("Password must have at least 2 digits");
    }

    if (isValid) {
        console.log('Password is valid');
    }

}


solve('logIn2')