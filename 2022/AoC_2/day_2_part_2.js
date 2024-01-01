const ROCK = "A";
const PAPER = "B";
const SCISSORS = "C";

const LOSE_POINTS = 0;
const DRAW_POINTS = 3;
const WIN_POINTS = 6;

const LOSE = "X";
const DRAW = "Y";
const WIN = "Z";

const fs = require('fs');


const fileContent = fs.readFileSync('input.txt', 'utf8');
const lines = fileContent.split('\n'); 


const chooseShape = (you,me) => {
    
    const shapeChoiceWin = {
        [ROCK]: PAPER,
        [PAPER]: SCISSORS,
        [SCISSORS]: ROCK
    };
    const shapeChoiceLose = {
        [ROCK]: SCISSORS,
        [PAPER]: ROCK,
        [SCISSORS]: PAPER
    };

    
    if (me === DRAW) {
        return you;
    } else if (me === WIN) {
        return shapeChoiceWin[you];
    } else {
        return shapeChoiceLose[you];
    }
}

resultScore = (you,me) => {
    if (you === me) {
        return DRAW_POINTS;
    } else if ((you === ROCK && me === PAPER) || (you === PAPER && me === SCISSORS) || (you === SCISSORS && me === ROCK)){
        return WIN_POINTS;
    } else {
        return LOSE_POINTS;
    }
}

const shapeScore = (myShape) => {
    let score = {[ROCK]:1, [PAPER]:2, [SCISSORS]:3 }
    return score[myShape]
}

let ans = 0;
lines.forEach(line => {
    let [yourShape, myShape] = line.split(" ");
    myShape = chooseShape(yourShape,myShape)
    ans += resultScore(yourShape, myShape) + shapeScore(myShape)
})

console.log(ans)