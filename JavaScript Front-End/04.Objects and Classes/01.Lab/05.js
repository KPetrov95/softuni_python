function solve(names) {
    const phoneBook = {}
    
    for (const line of names) {
        const [name, phone] = line.split(' ')
        phoneBook[name] = phone
    }
    
    for (const key in phoneBook) {
        console.log(`${key} -> ${phoneBook[key]}`);
    }

}