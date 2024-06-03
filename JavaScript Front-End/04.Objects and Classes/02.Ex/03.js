function solve(initial, order) {
    const products = {};

    for (let i = 0; i < initial.length; i += 2) {
        const product = initial[i];
        const qty = Number(initial[i + 1]);

        products[product] = qty;
    }
    
    for (let i = 0; i < order.length; i += 2) {
        const product = order[i];
        const qty = Number(order[i + 1]);

        if (!products[product]) {
            products[product] = 0;
        }
        
        products[product] += qty;
    }

    for (const product in products) {
        console.log(`${product} -> ${products[product]}`);
    }
}

solve([
    'Chips', '5', 'CocaCola', '9', 'Bananas', '14', 'Pasta', '4', 'Beer', '2'
],
    [
        'Flour', '44', 'Oil', '12', 'Pasta', '7', 'Tomatoes', '70', 'Bananas', '30'
    ]
)