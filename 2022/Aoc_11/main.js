const fs = require("fs");

const fileContent = fs.readFileSync("input_on.txt", "utf8");
const data = fileContent.split("\n\n");

const monkeys = [];
class Monkey {
  constructor(items, operation, test, ifTrue, ifFalse) {
    this.items = items;
    this.operation = operation;
    this.test = test;
    this.ifTrue = ifTrue;
    this.ifFalse = ifFalse;
    this.inspected = 0
  }

  proccessItem(item) {
    this.inspected+=1
    let newItem;

    let operationParts = this.operation.split(" ");
    let operator = operationParts[1];
    let operationValue = operationParts[2];

    if (operationValue === "old") {
      operationValue = item;
    } else {
        operationValue = Number(operationValue);
    }

    if (operator === "*") {
      newItem = item * operationValue;
    } else if (operator === "+") {
      newItem = item + operationValue;
    }
    return newItem
  }
  throwItems () {
    let newItems = [];

    this.items.forEach(item => {

        let proccessedItem = Math.floor(this.proccessItem(item)/3)
    
        let targetMonkeyIndex = proccessedItem % this.test === 0 ? this.ifTrue: this.ifFalse
        
        newItems.push({item: proccessedItem,targetMonkeyIndex})
    })
    newItems.forEach(({item,targetMonkeyIndex}) => {
        monkeys[targetMonkeyIndex].items.push(item)  
        })
    this.items = [];
    }
}


// Parsing monkeys from input
data.forEach(monkey => {
    let lines = monkey.split("\n")
    // console.log(lines)
    const items = lines[1].split(": ")[1].split(", ").map(Number)
    const test = lines[3].split(": ")[1].split(" ").slice(-1).map(Number)
    const ifTrue = lines[4].split(": ")[1].split(" ").slice(-1).map(Number);
    const ifFalse = lines[5].split(": ")[1].split(" ").slice(-1).map(Number);
    const operation = lines[2].split("= ")[1]
    // console.log(operation);

    monkey =new Monkey(items,operation,test,ifTrue,ifFalse)
    monkeys.push(monkey)
})
// console.log(monkeys)



for (let i =0; i< 20; i++){
    monkeys.forEach(monkey => {
        monkey.throwItems()
    })
}

// monkeys.forEach(monkey =>
//     console.log(monkey.items))



monkeys.sort((monkey1, monkey2) => monkey1.inspected - monkey2.inspected)

monkeys.forEach((monkey, index) => {
  console.log(`Monkey ${index}:`, monkey.items, monkey.inspected);
});

const ans = monkeys[monkeys.length -1].inspected * monkeys[monkeys.length-2].inspected
console.log(ans)