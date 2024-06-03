function solve(numberOfPeople, typeOfGroup, dayOfTheWeek) {
    let priceForOne;
    
    if (typeOfGroup === 'Students') {
        if (dayOfTheWeek === 'Friday') {
            priceForOne = 8.45;
        }
        else if (dayOfTheWeek === 'Saturday') {
            priceForOne = 9.80;
        }
        else if (dayOfTheWeek === 'Sunday') {
            priceForOne = 10.46;
        }
    }
    else if (typeOfGroup === 'Business') {
        if (dayOfTheWeek === 'Friday') {
            priceForOne = 10.90;
        }
        else if (dayOfTheWeek === 'Saturday') {
            priceForOne = 15.60;
        }
        else if (dayOfTheWeek === 'Sunday') {
            priceForOne = 16;
        }
    }
    else if (typeOfGroup === 'Regular') {
        if (dayOfTheWeek === 'Friday') {
            priceForOne = 15;
        }
        else if (dayOfTheWeek === 'Saturday') {
            priceForOne = 20;
        }
        else if (dayOfTheWeek === 'Sunday') {
            priceForOne = 22.50 ;
        }
    }
    let finalPrice = priceForOne * numberOfPeople

    if (typeOfGroup === 'Students' && numberOfPeople >= 30) {
        finalPrice *= 0.85
    }
    else if (typeOfGroup === 'Business' && numberOfPeople >= 100) {
        finalPrice -= priceForOne * 10
    }
    else if (typeOfGroup === 'Regular' && (numberOfPeople >= 10 && numberOfPeople <= 20)) {
        finalPrice *= 0.95
    }
    console.log(`Total price: ${finalPrice.toFixed(2)}`)
}

solve(40,
    "Regular",
    "Saturday"    
    )