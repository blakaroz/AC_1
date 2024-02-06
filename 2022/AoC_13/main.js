const fs = require("fs");


const fileContent = fs.readFileSync("input_on.txt", "utf8");
const parts = fileContent.split("\n\n");

const  compare = (left,right) =>{
  if (!Array.isArray(left) && Array.isArray(right)) {
    left = [left];
  }
  if (Array.isArray(left) && !Array.isArray(right)) {
    right = [right];
  }
  //base case
  if (!Array.isArray(left) && !Array.isArray(right)) {
    if (left < right){
      return 1;
    } else if (left=== right) {
      return 0;
    } else {
    return -1;
    }
  }
  
  if(Array.isArray(left) && Array.isArray(right)) {
    let i = 0;
    //recursion part
    while (i < left.length && i < right.length) {
      let result = compare(left[i], right[i]);
      if (result === 1 || result === -1) {
        return result;
      }
      i++; // jesli sa takie same to pomin - nie licą się - idziemy do kolejngo elementu
    }
    if (left.length !== right.length) {
      return left.length < right.length ? 1 : -1;
    }
    return 0;
  }

    // if (i === left.length){ // czyi jesli sprawdzilsimy wszsytkie elementy w ilosci takiej jakie mialy oba jednosczenise to spr czy to left bylo koniec
    //   if( left.length === right.length) {
    //     return 0 // skonczyly sie jednocznie oba i sa takie same na koncu -  idziemy dalej
    //   }
    //   return 1 // czyli lewa sie juz skonczyla a prawa jeszcze jest, tzn ze sa w dobrej kolejnosci 
    // } 
    // return -1 // czyli jesli to nie koniec a to znaczy ze to juz b sie skonczyło, czyli są w złej kolejności
    // }
  
}



let ans = 0;
for(i = 0; i<parts.length; i++) {
  let [left, right] = eval(`[${parts[i].split("\n")}]`);
  // let [left,right] = eval(parts[i].split("\n")) // eval on this
  
  if(compare(left,right) === 1) {
    ans += i + 1
  }
  

}

console.log(ans)