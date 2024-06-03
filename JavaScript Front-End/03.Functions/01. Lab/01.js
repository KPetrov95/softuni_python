function solve(grade) {
    let formatedGrade = ''

    if (grade < 3) {
        formatedGrade = `Fail (${grade})`;
    } else if (grade < 3.5) {
        formatedGrade = `Poor (${grade.toFixed(2)})`;
    } else if (grade < 4.5) {
        formatedGrade = `Good (${grade.toFixed(2)})`;
    } else if (grade < 5.5) {
        formatedGrade = `Very good (${grade.toFixed(2)})`;
    } else {
        formatedGrade = `Excellent (${grade.toFixed(2)})`;
    }  
    return formatedGrade
}

console.log(solve(2.9));