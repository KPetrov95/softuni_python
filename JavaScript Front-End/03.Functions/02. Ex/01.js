function solve(...nums) {
    let min_num = Number.MAX_SAFE_INTEGER
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] < min_num) {
            min_num = nums[i];
        }
    }
    return min_num
}

console.log((solve(1, 2, 3)));