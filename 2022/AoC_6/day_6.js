const fs = require('fs');
const fileContent = fs.readFileSync('input_ex.txt', 'utf8');
const data = fileContent;
console.log(data)

let notFound = true
while (notFound) {
    for (let i=0; i<data.length; i++) {
        let charBox = data.slice(i,(i+4))
        // console.log(charBox)
        if (charBox.length === new Set(charBox).size) {
            console.log(charBox)
            idx = data.indexOf(charBox)+14
            console.log(idx)
            notFound = false
            break
        }
    }
}
