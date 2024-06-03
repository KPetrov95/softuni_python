function solve(onex, oney, twox, twoy) {

    function distance(x1, y1, x2, y2) {
        const result = Math.sqrt((x1 - x2)**2 + (y1 - y2)**2);
        if (Number.isInteger(result)) {
        return `{${x1}, ${y1}} to {${x2}, ${y2}} is valid`
        }
        return `{${x1}, ${y1}} to {${x2}, ${y2}} is invalid`
    }

   console.log(distance(onex,oney, 0, 0));
   console.log(distance(twox,twoy, 0, 0));
   console.log(distance(onex,oney, twox, twoy));
    
}

solve(2, 1, 1, 1)