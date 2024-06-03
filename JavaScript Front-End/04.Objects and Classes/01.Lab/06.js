function solve(input) {
    const schedule = {}

    for (const line of input) {
            const [key, value] = line.split(' ');
            if (schedule[key]) {
                console.log(`Conflict on ${key}!`);
            } else {
                schedule[key] = value
                console.log(`Scheduled for ${key}`); 
            }
        }
    
        for (const key in schedule) {
            console.log(`${key} -> ${schedule[key]}`);
        }
}

solve(['Monday Peter',
'Wednesday Bill',
'Monday Tim',
'Friday Tim']
)