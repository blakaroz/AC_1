const fs = require('fs');
const fileContent = fs.readFileSync('input_ex.txt', 'utf8');
const data = fileContent.split('\n');

console.log(data)

