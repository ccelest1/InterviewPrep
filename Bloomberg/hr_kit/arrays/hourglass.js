/*

hourglass in given 2d array, is a subset of vals
    falling in pattern of arr's graphical representation
        abc
         d
        efg
          -> to detect this hourglass, rows = arr.length, cols = arr[0].length
          for i in range(0, rows, 3):
            for j in range(0, cols, 3)):
              if(
                rows[i][j] and rows[i][j+1] and rows[i][j+2]
                and rows[i+1][j+2]
                and rows[i+2][j] and rows[i+2][j+1] and rows[i+2][j+2]
              )

*/
var hourglassSum = function (arr) {
    const rows = arr.length
    const cols = arr[0].length
    let maxsum = -63;
    for (let i = 0; i < rows - 2; i++) {
        for (let j = 0; j < cols - 2; j++) {
            let boundarysum = arr[i][j] + arr[i][j + 1] + arr[i][j + 2]
                + arr[i + 1][j + 1]
                + arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
            if (boundarysum > maxsum) {
                maxsum = boundarysum
            }
        }
    }
    return maxsum;
}

// console.log(hourglassSum([
//     [1, 1, 1, 0, 0, 0],
//     [0, 1, 0, 0, 0, 0],
//     [1, 1, 1, 0, 0, 0],
//     [0, 0, 2, 4, 4, 0],
//     [0, 0, 0, 2, 0, 0],
//     [0, 0, 1, 2, 4, 0]
// ]
// ))
// // returns 19

// console.log(hourglassSum([
//     [- 9, -9, -9, 1, 1, 1],
//     [0, -9, 0, 4, 3, 2],
//     [-9, -9, -9, 1, 2, 3],
//     [0, 0, 8, 6, 6, 0],
//     [0, 0, 0, -2, 0, 0],
//     [0, 0, 1, 2, 4, 0]
// ]
// ))
// // needs to return 28

// console.log(hourglassSum([
//     [1, 1, 1, 0, 0, 0],
//     [0, 1, 0, 0, 0, 0],
//     [1, 1, 1, 0, 0, 0],
//     [0, 9, 2, -4, -4, 0],
//     [0, 0, 0, -2, 0, 0],
//     [0, 0, -1, -2, -4, 0]
// ]
// ))
// needs to return 13

console.log(hourglassSum([
    [0, -4, -6, 0, -7, -6],
    [-1, -2, -6, -8, -3, -1],
    [-8, -4, -2, -8, -8, -6],
    [-3, -1, -2, -5, -7, -4],
    [-3, -5, -3, -6, -6, -6],
    [-3, -6, 0, -8, -6, -7]
]
))
