/**
 * @param {number} n
 * @param {number[]} ar
 * @return {number}
 */
var sockMerchant = function (n, ar) {
    let pairs = 0;
    if (ar.length <= 1 || n <= 1) {
        return 0;
    }
    let tracker = {}
    for (let r = 0; r < n; r++) {
        tracker[ar[r]] = 1 + (tracker[ar[r]] || 0)
    }
    for (let val of Object.values(tracker)) {
        if (val > 1) {
            let pair = Math.floor(val / 2)
            pairs += pair
        }
    }
    return pairs

}
console.log(sockMerchant(
    7,
    [1, 2, 1, 2, 1, 3, 2]
))
