function solve(input) {
    const dictionary = {}
    const entries = input.map(JSON.parse)

    for (const entry of entries) {
        const def = Object.keys(entry);
        dictionary[def] = entry[def];
    }

    Object.entries(dictionary)
        .sort((a, b) => a[0].localeCompare(b[0]))
        .forEach(([term, definition]) => console.log(`Term: ${term} => Definition: ${definition}`));
}