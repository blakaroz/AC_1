const fs = require('fs');


const fileContent = fs.readFileSync('input_ex.txt', 'utf8');
const data = fileContent.split('\n'); 

console.log(data)

let dataRanges = [];

data.forEach(line => {
    let pairs = line.split(",");
    let pairsRange = []
    pairs.forEach(pair => {
        let [start, end] = pair.split("-").map(Number)
        let range = [];
            for(i = start; i <=end ; i++) {
                range.push(i)
            }
        pairsRange.push(range)
    })
    // console.log(pair)
    dataRanges.push(pairsRange)
})

console.log(dataRanges)


// Function to chech two section and take all elements from arr to check if they are in second arr.
const isSectioninSection = (section1,section2) => {
    return section1.every(element => section2.includes(element));
}

const isSomeSectioninSection = (section1,section2) => {
    return section1.some(element => section2.includes(element));
}

// filter?
// set?



let ans1 = 0;
let ans2 = 0;
dataRanges.forEach(pair => {
    section1 = pair[0];
    section2 = pair[1];
    // wrong because i have to use single element - not whole array to check
    // if (section1.inludes(section2) || section2.includes(section1)){
    //     ans1 += 1
    // }
    if (isSectioninSection(section1,section2) || isSectioninSection(section2,section1)){
        ans1 +=1
    }
    if (isSomeSectioninSection(section1,section2) || isSomeSectioninSection(section2,section1)){
        ans2 +=1
    }
})

console.log(ans1)
console.log(ans2)