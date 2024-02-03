#failed with recursion for now :(

with open("input_ex.txt") as file:
    grid = [list (x) for x in file.read().strip().splitlines()]

for r,row in enumerate(grid):
    for c,item in enumerate(row):
        # print(item)
        if item == "S":
            sr = r
            sc = c
            #changing "S" to easy manipulate going steps and no trickt s as different from others
            grid[r][c] = "a"
        
        if item == "E":
            er =r
            ec = c
            grid[r][c] = "z"


visited = set()


def find_path(r,c,previous_char_grid):
    #base cases

    #1. off the grid:
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
        return False
    #2. already seen:
    if (r,c) in visited:
        return False
    #3. if step > 1
    if ord(grid[r][c]) - ord(previous_char_grid) > 1:
        return False
    #4. have an end:
    if grid[r][c] == "z":
        return [(r,c)]
    
    visited.add((r,c))

    #visit neightbours:
    for nr, nc in [(r+1, c), (r-1,c), (r,c+1), (r,c-1)]:
        path = find_path(nr,nc, grid[r][c])
        if path:
            return [(r,c)] + path
    return False

path = find_path(sr,sc, "a")
    

if path:
    print("Path found:", path)
else:
    print("No path found.")
print(len(path))