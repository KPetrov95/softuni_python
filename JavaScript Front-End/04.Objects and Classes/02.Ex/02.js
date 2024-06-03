function solve(input) {
    const towns = []
    for (line of input) {
        const [name, lat, long] = line.split(' | ')
        const town = {
            town: name,
            latitude: Number(lat).toFixed(2),
            longitude: Number(long).toFixed(2)
        }
        towns.push(town)
    }

    towns.forEach(town => console.log(town));
}

solve(['Sofia | 42.696552 | 23.32601',
'Beijing | 39.913818 | 116.363625']
)