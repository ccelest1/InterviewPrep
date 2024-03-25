/*
given two strings, a and b (may be of same length)
determine min number of char deletions req t make a, b anagrams of each other
any chars can be deleted from either of strings

input: a:str, b:str -> output: int (min # of char deletions required to make a and b anagrams of each other)
 */
/**
 *
 * @param {string} a
 * @param {string} b
 */
function makeAnagram(a, b) {
    let count = Array(26).fill(0)
    let deletions = 0
    if (
        a.length == 1 && b.length == 1 &&
        a !== b
    ) {
        return
    }
    for (let i of a) {
        count[i.charCodeAt(0) - 'a'.charCodeAt(0)] += 1
    }
    for (let j of b) {
        count[j.charCodeAt(0) - 'a'.charCodeAt(0)] -= 1
    }
    for (let num of count) {
        if (num !== 0) {
            deletions += Math.abs(num)
        }
    }
    return deletions
}

console.log(makeAnagram(
    'cde', 'dcf'
))
console.log(makeAnagram(
    'cde', 'abc'
))
