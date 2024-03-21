/**
 * @param {number[]} c
 * @returns {number}
 */
var jumpingOnClouds = function (c) {
    let jumps = 0
    const clouds_length = c.length
    if (clouds_length <= 1) {
        return jumps
    }
    // determine if one can jump 1 or 2 clouds
    let cloudIndex = 0;
    while (cloudIndex < clouds_length) {
        if (c[cloudIndex] === clouds_length) {
            return jumps
        }
        if (c[cloudIndex] !== c[cloudIndex + 1]) {
            if (
                c[cloudIndex + 2] < clouds_length && c[cloudIndex] == c[cloudIndex + 2]
            ) {
                jumps += 1
                cloudIndex += 2
            } else {
                break
            }
        } else {
            if (c[cloudIndex + 2] < clouds_length && c[cloudIndex] == c[cloudIndex + 2]) {
                jumps += 1
                cloudIndex += 2
            } else {
                jumps += 1
                cloudIndex += 1
            }
        }
    }
    return jumps
}

console.log(
    jumpingOnClouds(
        [0, 1, 0, 0, 0, 1, 0]
    )
)
