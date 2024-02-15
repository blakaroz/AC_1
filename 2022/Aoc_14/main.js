const fs = require("fs");


const fileContent = fs.readFileSync("input_ex.txt", "utf8");
const data = fileContent.split("\n");

console.log(data)

const filled = new Set ();

data.forEach(line => {
 
  
  const segments = line.split(" -> ").map(segment => segment.split(",").map(Number))

  for (let i =0; i< segments.length -1; i++) {

  
    const [cx,cy] = segments[i];
    const [px,py] = segments[i+1];

    if(cy === py) {
      for (let x= Math.min(cx,px); x < Math.max(cx,px)+1; x++) {
        filled.add(`${x},${cy}`);
      }
    }
    if(cx === px) {
      for (let y = Math.min(cy,py); y < Math.max(cy,py) +1; y++) {
        filled.add(`${cx},${y}`)
      }
    }
  }

  
})
console.log(Array.from(filled))

const maxY = Math.max(filled.map(coord => coord[1])) 
console.log(maxY)
const sandCord = [500,0];

const sandFalling = () => {
  let [x,y] = sandCord;

  // while (y < maxY)

}
