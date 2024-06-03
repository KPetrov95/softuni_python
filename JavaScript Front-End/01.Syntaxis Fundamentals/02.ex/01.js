function solve(age) {
    let result = 'out of bounds';
    if (age >= 66) {
        result = 'elder';
    }
    else if (age >= 20) {
        result = 'adult';
    }
    else if (age >= 14) {
        result = 'teenager';
    }
    else if (age >= 3) {
        result = 'child';
    }
    else if (age >= 0) {
        result= 'baby';
    }
    console.log(result);
}

solve(66)
solve(14)
solve(3)
solve(0)