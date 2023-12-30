with open("data.txt") as file:
    data = file.read()
    grid = data.split('\n')


# 1. search for coordinates of symbol (not a '.')
# 2. check if around isdigit (if not just continue searching)
# 3. find start of the string of digit (numbers)
# 4. find whole string of digit
# 5. find the total sum of all that numbers 


cs = set()

for r, row in enumerate(grid):
    for c, char in enumerate(row):
        if char.isdigit() or char == ".":
            continue
        for cr in [r-1,r,r+1]:
            for cc in [c-1,c,c+1]:
                if cr <0 or cr >= len(grid) or cc <0 or cc >=len(grid[cr]) or not grid[cr][cc].isdigit():
                    continue
                while cc > 0 and grid[cr][cc-1].isdigit():
                    cc -=1
            
                cs.add((cr,cc))




total = 0
for r,c in cs:
    string = ""
    while c < len(grid[r]) and grid[r][c].isdigit():
        string += grid[r][c]
        c += 1
    total += int(string)


print(total)

                
