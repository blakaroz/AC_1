const fs = require('fs');
const fileContent = fs.readFileSync('input.txt', 'utf8');
const data = fileContent.split('\n'); 

// console.log(data)

let operationDict = {"move": [], "from": [], "to": []}


data.forEach(line => {
    let [move, how_many, froom, where_from, to, where_to] = line.split(" ")
    operationDict["move"].push(Number(how_many))
    operationDict["from"].push(Number(where_from))
    operationDict["to"].push(Number(where_to))
})
// console.log(operationDict)

contenersDictTask1 = [["Z", "N"],["M", "C", "D"],["P"]]

contenersDictTask = [["F","T","C","L","R","P","G","Q"],
    ["N","Q","H","W","R","F","S","J"],
    ["F","B","H","W","P","M","Q"],
    ["V","S","T","D","F"],
    ["Q","L","D","W","V","F","Z"],
    ["Z","C","L","S"],
    ["Z","B","M","V","D","F"],
    ["T","J","B"],
    ["Q","N","B","G","L","S","P","H"]]


    for (let i = 0; i < operationDict["move"].length; i++){
        let whereFrom = operationDict["from"][i] - 1
        let howMany = operationDict["move"][i] 
        let whereTo = operationDict["to"][i] -1

        // for (let _ = 0; _ < howMany; _ ++) {
        //     let remove = contenersDictTask[whereFrom].pop()
        //     contenersDictTask[whereTo].push(remove)
        // }

        // for (let _ = 0; _ < howMany; _ ++) {
        let elementsToMove = contenersDictTask[whereFrom].slice(-howMany)
        contenersDictTask[whereFrom].splice(-howMany)
        // console.log(elementsToMove)
        elementsToMove.forEach(element => {
        contenersDictTask[whereTo].push(element)
        } )
        
        
    }

    // console.log(contenersDictTask)

    let ans = ""
    contenersDictTask.forEach(element => {
        ans += element[element.length -1]
    })
    console.log(ans)

