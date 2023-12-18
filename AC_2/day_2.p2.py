
with open("data.txt") as file:
    data = file.read().strip().split("\n")

total = 0

for line in data:
    game, parts = line.split(": ")
    game_id = int(game.split()[1])

    red,blue,green = 0,0,0
  
    for part in parts.split("; "):
        
        for cubes in part.split(", "):
            num, color = cubes.split()
            num = int(num)
            
            if color == "red":
                 red = max(red, num)
            if color == "blue":
                blue = max(blue, num)
            if color == "green":
                green = max(green, num)
    total += red * blue * green 
    
print(total)



