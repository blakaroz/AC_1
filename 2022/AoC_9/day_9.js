const fs = require('fs');
const fileContent = fs.readFileSync('input_task.txt', 'utf8');
const movements = fileContent.split('\n');

let counter =  new Set(['0,0']);

let H = [0,0];
let T = [0,0];

for (let line of movements) {
    let [direction, howMany] = line.split(" ")
    
    howMany = parseInt(howMany)

    for (let i = 0; i < howMany; i++) {
        let directionX = direction === "R" ? 1 : direction === "L" ? -1 : 0;
        
        let directionY = direction === "D" ? 1 : direction === "U" ? -1 : 0;
    
        H[0] += directionX
        H[1] += directionY

        let distanceX  = H[0] - T[0];
        let distanceY = H[1] - T[1];

        if (Math.abs(distanceX) > 1 || Math.abs(distanceY) > 1) {
            if (distanceX === 0){
                T[1] += distanceY >0 ? 1: -1
            }
            else if (distanceY === 0){
                T[0] += distanceX > 0 ? 1 : -1
            }
            else {
                T[0] += distanceX > 0 ? 1 : -1
                T[1] += distanceY > 0 ? 1 : -1
            }
            counter.add([T[0], T[1]].toString())
        }
    }
}
console.log(counter.size)
