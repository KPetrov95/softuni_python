function solve(a, b, sign) {
    switch(sign) {
        case '+': console.log(a + b); break;
        case '-': console.log(a - b); break;
        case '*': console.log(a * b); break;
        case '/': console.log(a / b); break;
        case '%': console.log(a % b); break;
        case '**': console.log(a ** b); break;
        }
}

solve(5, 6, '+')
solve(3, 5.5, '*')