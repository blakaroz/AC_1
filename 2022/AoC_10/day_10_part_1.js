const fs = require("fs");
const program = fs.readFileSync("input_on.txt", "utf8");



// Utworz array z osobno dostepna nazwa instrukcji cycleNumber osobno liczba do dodania (sformatowany string na liczbe)
let instructions = program.split("\n").map(element => {
    let parts = element.trim().split(" ");
    if (parts[1]) {
        parts[1] = parseFloat(parts[1])
    }
    return parts
})

// console.log(instructions)
// Array z dostepem do kolejnych instrukcji cycleNumber wartosci jezeli jest dana
let database = []


let cycleNumber = 1; //cykle number
let X = 1;
instructions.forEach(instruction => {
    
    if (instruction[0] === "noop"){
        database.push([cycleNumber,X])
        cycleNumber++
    } else {
        
        database.push([cycleNumber, X]);
        cycleNumber++;
        X += instruction[1]
        database.push([cycleNumber, X]);

        // database.push([cycleNumber, instruction[1]])
        cycleNumber++
    }

})
// console.log(database)



let cycle = [20,60,100,140,180,220] 
//dla nich wartosc razy to 
sum = 0
cycle.forEach(element => {
    let index = element -2
    sum += element * database[index][1]
    console.log(element, database[index][1],sum);

})

console.log(sum)


// fs.writeFileSync("output.txt", JSON.stringify(database, null, 2));
