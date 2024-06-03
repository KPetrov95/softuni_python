function solve(jsonString) {
    newObject = JSON.parse(jsonString)
    Object.keys(newObject).forEach(key => console.log(`${key}: ${newObject[key]}`))
}

solve('{"name": "George", "age": 40, "town": "Sofia"}')