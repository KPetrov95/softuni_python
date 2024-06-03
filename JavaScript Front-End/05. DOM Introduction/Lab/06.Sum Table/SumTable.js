function sumTable() {
    const costElements = document.querySelectorAll('tr td:last-of-type:not(#sum)');
    let field = document.querySelector('#sum')
    const sum =Array
        .from(costElements)
        .reduce((sum, num) => sum + Number(num.textContent), 0);
    
    field.textContent = sum
}