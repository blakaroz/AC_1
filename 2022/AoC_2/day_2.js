const fs = require('fs');

const fileContent = fs.readFileSync('input.txt', 'utf8');
const lines = fileContent.split('\n'); 

const LOSE_POINTS = 0;
const DRAW_POINTS = 3;
const WIN_POINTS = 6;


const replacement_dic = {"A":"X", "B":"Y", "C":"Z"};


resultScore = (you,me) => {
    if (you === me) {
        return DRAW_POINTS;
    } else if ((you === "X" && me === "Y") || (you === "Y" && me === "Z") || (you === "Z" && me === "X")){
        return WIN_POINTS;
    } else {
        return LOSE_POINTS;
    }
}


shapeScore = (myShape) => {
    const score = {"X":1, "Y":2, "Z":3}
    return score[myShape];
}


console.log(lines)


let ans = 0;

lines.forEach(line => {
    const [yourChoice,myChoice] = line.split(" ");
    console.log(yourChoice);
    console.log(myChoice);
    const you = replacement_dic[yourChoice];
    console.log(resultScore(you,myChoice));
    console.log("");
    console.log(shapeScore(myChoice));

    ans += resultScore(you,myChoice) + shapeScore(myChoice);
});

console.log(ans)