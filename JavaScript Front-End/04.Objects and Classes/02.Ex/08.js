function solve(input) {
    const parking = {};
    
    for (const line of input) {
        const [command, plate] = line.split(', ')
        
        command === 'IN'
            ? parking[plate] = true
            : delete parking[plate]
    }
    if (parking.size < 1) {
        return console.log('Parking Lot is Empty');
    }
    Object.keys(parking)
        .sort((a, b) => a.localeCompare(b))
        .forEach(number => console.log(number));
 
}

solve(['IN, CA2844AA',
'IN, CA1234TA',
'OUT, CA2844AA',
'IN, CA9999TT',
'IN, CA2866HI',
'OUT, CA1234TA',
'IN, CA2844AA',
'OUT, CA2866HI',
'IN, CA9876HH',
'IN, CA2822UU']
)