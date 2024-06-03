function solve(a, b, c) {
    const nums = [a, b, c];
    function isNegative(nums) {
        filtered_nums = nums.filter((num) => num < 0)
        return filtered_nums.length % 2 == 0;
    }

    if (isNegative(nums)) {
        return 'Positive'    
    }
    else {
        return 'Negative'
    }
}

console.log(solve(1, -2, -3));