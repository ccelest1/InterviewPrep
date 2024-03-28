/*
    given budget, cost of each flavor for t trips to parlor
    return 2 distinct flavors to deplete budget
    ID #s are 1-based index # associated with cost

    For each parlor trip, print id numbers for both ice cream types purchases as two space separated integers on new line
    Print smaller id first, larger second
*/
/**
 *
 * @param {number[]} cost
 * @param {int} money
 * @returns {int}
 */
function whatFlavors(cost, money) {
    const tracker = {}
    let remainder;
    for (const [index, element] of cost.entries()) {
        remainder = money - element
        if (Object.keys(tracker).includes(String(element))) {
            console.log(tracker[remainder] + 1, index + 1)
        } else {
            tracker[element] = index
        }
    }
}

function whatFlavors2(cost, money) {
    const tracker = {};
    let remainder;
    for (let i = 0; i < cost.length; i++) {
        remainder = money - cost[i];
        if (tracker.hasOwnProperty(remainder)) {
            console.log(tracker[remainder] + 1, i + 1)
        } else {
            tracker[cost[i]] = i;
        }
    }
    return -1;
}

console.log(whatFlavors(
    [1, 4, 5, 3, 2],
    4
))
