/*

    Given words in magazine and words in ransom note, return Yes if he can replicate ransom note using magazine else print no
    Must use entire whole words, strict about case sensitivity

    ex: magazine:'attack at dawn', note:'Attack at dawn'

    Parameters:
        input: string (magazine). string(note)
        output: 'yes' or 'no'

    handling duplicates
    note, attack attack dawn
         attack at dawn
 */
function checkMagazine(magazine, note) {
    if (
        magazine.length == 0 || note.length == 0
        || magazine.length < note.length
    ) {
        console.log('No')
        return
    }
    let tracker_m = {}
    for (let m of magazine) {
        tracker_m[m] = (tracker_m[m] || 0) + 1
    }
    let n = 0;
    console.log(tracker_m)
    while (n <= note.length - 1) {
        let word = note[n]
        if (tracker_m[word] && tracker_m[word] >= 1) {
            tracker_m[word] -= 1
            if (n == note.length - 1) {
                console.log('Yes')
                break
            }
            n += 1
        } else {
            console.log('No')
            break
        }
    }
}

// console.log(checkMagazine(
//     ['give', 'me', 'one', 'grand', 'today', 'night'],
//     ['give', 'one', 'grand', 'today']
// ))

console.log(checkMagazine(
    ["o", "l", "x", "imjaw", "bee", "khmla", "v", "o", "v", "o", "imjaw", "l", "khmla", "imjaw", "x"],
    ["imjaw", "l", "khmla", "x", "imjaw", "o", "l", "l", "o", "khmla", "v", "bee", "o", "o", "imjaw", "imjaw", "o"]
))
