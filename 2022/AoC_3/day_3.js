const fs = require('fs');

const fileContent = fs.readFileSync('input.txt', 'utf8');
const rucksacks = fileContent.split('\n'); 

const ascii = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
const priorityDict = {};
for (let i = 0; i < ascii.length; i++) {
    priorityDict[ascii[i]] = i+1;
}

let totalSum = 0;
rucksacks.forEach(rucksack => {
    const half = Math.floor(rucksack.length/2);
    const pocket1 = rucksack.substring(0,half);
    const pocket2= rucksack.substring(half);
    
    // ... robi  z string lub set [...pocket] array z wszystkimi wystapieniami pocket i robie to zeby moc uzyc fuknci array czyi filter
    // a pocket2.includes(char) to funkcja na stringu i moge tak o
    const same = new Set([...pocket1].filter(char => pocket2.includes(char)))


totalSum += [...same].reduce((acc, char) => acc + priorityDict[char],0)

})

// Part 2


let totalSum2 = 0;

for (let i = 0; i < rucksacks.length; i+= 3) {
    let group = rucksacks.slice(i, i+3);
  
    // split one group to crate array of contains chars to be able to use filter on this data
    // check for every char which of char is included in other groups and create a set to filter only unique values if it could be duplicates
    let sameChar = new Set(group[0].split("").filter(char => group[1].includes(char) && group[2].includes(char)));
    
    
    // change sameChar to array to use reduce method and sign value of priorityDic for every instance
    totalSum2 += [...sameChar].reduce((acc, char) => acc + priorityDict[char],0)
    
}

console.log(totalSum2)   
