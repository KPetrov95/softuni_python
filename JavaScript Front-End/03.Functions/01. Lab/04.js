function solve(product, qty) {
    function getPrice(product) {
        switch (product) {
            case 'coffee' :
                return 1.50
            case 'water' :
                return 1.00
            case 'coke' :
                return 1.40
            case 'snacks' :
                return 2.00
        }
    }
    const price = getPrice(product) * qty;
    return (price.toFixed(2))
}