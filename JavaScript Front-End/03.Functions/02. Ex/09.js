function solve(number) {
    let zeroBar = '.'.repeat(10);

    function fillBar(number) {
       let filledBar = zeroBar;
       for (let i = 0; i < number / 10; i++) {
        filledBar = filledBar.replace('.', '%');
       }
       return filledBar;
    }

    
    if (number === 100) {
        console.log('100% Complete!');
        console.log('[%%%%%%%%%%]');
    }else {
        console.log(`${number}% [${fillBar(number)}]`);
        console.log('Still loading...');
    }
}

solve(100)