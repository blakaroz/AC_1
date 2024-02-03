const fs = require("fs");


const fileContent = fs.readFileSync("input_on.txt", "utf8");
const data = fileContent.split("\n");

const grid = [];
data.forEach((line) => {
  line = line.split("");
  // console.log(line)
  grid.push(line);
});
// const grid = data.map(line => line.split("\n"))
// console.log(grid)

let sr, sc, er, ec;

// console.log(grid)
grid.forEach((row, r) => {
  row.forEach((item, c) => {
    if (item === "S") {
      sr = r;
      sc = c;
      grid[r][c] = "a";
    }
    if (item === "E") {
      er = r;
      ec = c;
      grid[r][c] = "z";
    }
  });
});

// console.log(`Start: (${sr}, ${sc}), End: (${er}, ${ec})`);

const q = [[0, sr, sc]];
const visited = new Set([`${sr},${sc}`]);
let found = false;

while (q.length > 0 && !found) {
  let [d, r, c] = q.shift();
  // console.log(d, r, c);
  let dir = [
    [r + 1, c],
    [r - 1, c],
    [r, c + 1],
    [r, c - 1],
  ];

    dir.forEach(([nr, nc]) => {
        if (nr < 0 || nr >= grid.length || nc < 0 || nc >= grid[0].length || visited.has(`${nr},${nc}`)) {
        // Skip if out of bounds or already visited
        return; // Correctly use return to skip this forEach iteration
        }
    
    // Checking character step condition
    if (grid[nr][nc].charCodeAt(0) - grid[r][c].charCodeAt(0) > 1) {
      return
    
    }
    if (nr === er && nc === ec) {
      console.log(`Found 'E' at distance: ${d + 1}`);
      found = true;
      return
    }
    visited.add(`${nr},${nc}`);
    q.push([d + 1, nr, nc]);
  })
}
