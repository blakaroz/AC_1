with open("data.txt") as file:
    data = file.read()
    grid = data.split('\n')

total = 0

for r, row in enumerate(grid):
    for c, char in enumerate(row):
        if char != "*":
            continue

        cs = set()

        for cr in [r-1,r,r+1]:
            for cc in [c-1,c,c+1]:
                if cr <0 or cr >= len(grid) or cc <0 or cc >=len(grid[cr]) or not grid[cr][cc].isdigit():
                    continue
                while cc > 0 and grid[cr][cc-1].isdigit():
                    cc -=1
            
                cs.add((cr,cc))
        if len(cs) != 2:
            continue



        list = []
        for row,column in cs:
            string = ""
            while column < len(grid[row]) and grid[row][column].isdigit():
                string += grid[row][column]
                column += 1
            list.append(int(string))
        total += list[0] * list[1]
print(total)

                
