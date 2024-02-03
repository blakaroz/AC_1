with open("input_on.txt") as file:
    grid = [list (x) for x in file.read().strip().splitlines()]

# print(grid)

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



# first append distance, coordinate from start
q=[(0,sr,sc)]

# track visited place set
visited = {(sr,sc)}

while q:
    #unpacck poping which will happend to pop from the que when sth is added
    d,r,c = q.pop(0)
    
    for nr, nc in [(r+1, c), (r-1,c), (r,c+1), (r,c-1)]:
        #checking if off grid or if 
        if nr < 0 or nr >= len(grid) or nc <0 or nc >= len(grid[0]):
            continue
        # checking if seen
        if (nr,nc) in visited:
            continue
        #checking if > 1 level (ord fun return num from char)
        if ord(grid[nr][nc]) - ord(grid[r][c]) > 1:
            continue
        #now we have valid input and we can check
        if nr == er and nc == ec:
            distance = d + 1
            print(distance)
            break
        visited.add((nr,nc))
        q.append((d+1,nr,nc))

# print(visited)
# print(q)


# 643 to high

#thinking about recursion


