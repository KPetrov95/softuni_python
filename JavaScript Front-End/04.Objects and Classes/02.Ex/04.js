function solve(input) {
    const movies = [];

    for (line of input) {
        addCommand = 'addMovie';
        directorCommand = 'directedBy';
        dateCommand = 'onDate';

        if (line.includes(addCommand)) {
            const movie = {
                name: line.substring(addCommand.length + 1),
            }
            movies.push(movie);
        }else if (line.includes(directorCommand)) {
            const [movieName, movieDirector] = line.split(` ${directorCommand} `)
            const movie = movies.find(movie => movie.name === movieName);
            if (movie) {
                movie.director = movieDirector;
            }
        }else if (line.includes(dateCommand)) {
            const [movieName, movieDate] = line.split(` ${dateCommand} `)
            const movie = movies.find(movie => movie.name === movieName);
            if (movie) {
                movie.date = movieDate;
            }
        }
    }
    movies
        .filter(movie => movie.director && movie.date)
        .forEach(movie => console.log((JSON.stringify(movie))));
}