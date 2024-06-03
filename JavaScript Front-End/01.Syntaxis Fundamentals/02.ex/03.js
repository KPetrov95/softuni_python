function solve(year) {
    let answer = 'no'
    if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)) {
        answer = 'yes'
    }
    console.log(answer)
}

solve(4)