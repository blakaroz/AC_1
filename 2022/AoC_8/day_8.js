const fs = require('fs');
const fileContent = fs.readFileSync('input.txt', 'utf8');
const data = fileContent.split('\n');


// Convert data to arrays of numbers
let grid = data.map(line => line.split("").map(number => parseInt(number)));

console.log(grid)

// let counter = 0; 


// for (let row = 0; row < grid.length; row ++) {
//     for (let column = 0; column < grid[row].length; column++){
//         let current = grid[row][column]
//         let left = grid[row].slice(0, column).every(x => x < current)
//         let right = grid[row].slice(column).every(x => x < current)
//         let up = grid.slice(0, row).every(row => row[column < current])
//         let down = grid.slice(row).every(row => row[column]<current)
        
//         if (left || right || up || down) {
//             counter +=1
//         }
//     }
// }
// console.log(counter)

// Part 2 
treeMax = 0;

for (let row = 0; row < grid.length; row ++) {
    for (let column = 0; column < grid[row].length; column++){
        let current = grid[row][column]
        let L=0, R=0, U=0, D =0;


        for (let l = column-1; l >= 0; l--) {
            L += 1;
            if (grid[row][l] >= current){
                break
            }
        }
        // (let r = column; r < column.length -1; r++ )
        for (let r = column+1; r < grid[row].length; r++ ){
            R += 1;
            if (grid[row][r] >= current) {
                break
            }
        }
        for (let u = row-1; u >= 0; u--){
            U +=1;
            if (grid[u][column]>=current) {
                break
            }
        }
        for (let d = row+1; d < grid.length; d++){
            D +=1;
            if (grid[d][column] >= current) {
                break
            }
        }
       
        let total = L * R * U * D
        // console.log(total)
        treeMax = Math.max(treeMax,total)


    
    
    }}
    console.log(treeMax)