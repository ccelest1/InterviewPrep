/*
    implement bubble sort
    then return first number of swaps then (2) first element and last element
    print three lines and return
 */

function countSwaps(a) {
    if (a.length <= 1) {
        return
    }

    const swap = (arr, first, second) => {
        return [arr[first], arr[second]] = [arr[second], arr[first]]
    }
    let swaps = 0
    var noSwaps;
    for (let i = a.length; i > 0; i--) {
        for (let j = 0; j < i - 1; j++) {
            if (a[j] > a[j + 1]) {
                swap(a, j, j + 1)
                swaps += 1
            }
        }
        if (noSwaps) {
            break
        }
    }
    let last = a[a.length - 1]
    let first = a[0]
    console.log(
        `Array is sorted in ${swaps} swaps.
First Element: ${first}
Last Element: ${last}`
    )
    return
}

console.log(countSwaps(
    [6, 4, 1]
))
