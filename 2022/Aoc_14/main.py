with open("input_on.txt") as file:
    data = file.read().strip().split("\n")

# print(data)

filled = set()

for line in data:
    coord = []

    for str_line in line.split(" -> "):
        x, y = map(int, str_line.split(","))
        coord.append((x,y))


    for i in range(1, len(coord)):
        cx,cy = coord[i]
        nx,ny = coord[i-1]
    
        #jesli ida po x to y sie nie zmienia i dodajemy ranga x
        if cy != ny:
            for y in range(min(cy,ny), max(cy,ny)+1):
                filled.add((cx,y))

        if cx != nx:
            for x in range(min(cx,nx), max(cx,nx)+1):
                filled.add((x,cy))

sand_coord = 500,0
#where we notice that send is falling off the stones
max_y = max( [coord[1] for coord in filled])
# print(max_y)
# print(filled)

def sand_falling():
    global filled
    x,y = 500,0
    while y < max_y:
        if (x,y+1) not in filled:
            y+=1
            continue
        if (x-1,y+1) not in filled:
            x-=1
            y+=1
            continue
        if (x+1,y+1) not in filled:
            x+=1
            y+=1
            continue

        filled.add((x,y))
        return True
    return False


sand_in_grid = True
ans = 0
while sand_in_grid:
    check_sand_in_grid = sand_falling()

    if check_sand_in_grid == False:
        break
    ans+=1

print(ans)