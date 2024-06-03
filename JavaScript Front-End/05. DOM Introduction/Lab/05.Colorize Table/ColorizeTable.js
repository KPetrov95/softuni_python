function colorize() {
    coloredCells = document.querySelectorAll('table tr:nth-child(2n)')
    for (cell of coloredCells){
        cell.style.backgroundColor = 'teal';
    }
}