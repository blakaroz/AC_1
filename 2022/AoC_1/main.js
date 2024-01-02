var fs = require('fs');
const fileContent = fs.readFileSync('input_ex.txt', 'utf8');
const groups = fileContent.trim().split('\n\n'); 

console.log(groups)

const data = groups.map(group => group.split("\n").map(Number));

console.log(data)
// console.log()

let sumOfGroups = data.map(group => group.reduce((acc, cv) => acc+ cv, 0));
console.log(sumOfGroups)
// const maxSum = Math.max(data.map(group => group.reduce((acc, cv) => acc+ cv, 0)))
const maxSum = Math.max(...sumOfGroups);
console.log(maxSum)


// Part 2

const sums = data.map(group => group.reduce((acc,cv) => acc + cv, 0));
