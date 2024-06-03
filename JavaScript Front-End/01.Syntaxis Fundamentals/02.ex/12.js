function solve(num, op1, op2, op3, op4, op5) {
    num = Number(num)
    let operations = op1[0] + op2[0] +op3[0] + op4[0] + op5[0]
    for (let i = 0; i < operations.length; i++) {
        switch(operations[i]) {
            case 'c':
                num = num / 2
                break
            case 'd':
                num = Math.sqrt(num)
                break
            case 's':
                num += 1
                break
            case 'b':
                num *= 3
                break
            case 'f':
                num -= num * 0.2
                break
        }
        console.log(num);
    }
}

solve('9', 'dice', 'spice', 'chop', 'bake', 'fillet')