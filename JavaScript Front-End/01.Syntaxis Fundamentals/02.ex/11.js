function solve(speed, area) {
    let speedLimit = 0 ;

    if (area == 'motorway') {
        speedLimit = 130;
    }
    else if (area == 'interstate') {
        speedLimit = 90;
    }
    else if (area == 'city') {
        speedLimit = 50;
    }
    else if (area == 'residential') {
        speedLimit = 20;
    }

    let difference = speed - speedLimit;
    let status = 'reckless driving'
    if (difference <= 0) {
        console.log(`Driving ${speed} km/h in a ${speedLimit} zone`)
    }
    else {
        if (difference <= 20) {
            status = 'speeding'
        }
        else if (difference <= 40) {
            status = 'excessive speeding'
        }
        console.log(`The speed is ${difference} km/h faster than the allowed speed of ${speedLimit} - ${status}`)
    }
}

solve(150, 'interstate')