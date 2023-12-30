with open("data.txt") as file:
    data = file.read().strip().split("\n")

total = 0
# ogarnij date zeby podzielic przez ; a 
for line in data:
    game, parts = line.split(": ")
    game_id = int(game.split()[1])

  
    can_play = True
    for part in parts.split("; "):
        
        for cubes in part.split(", "):
            num, color = cubes.split()
            num = int(num)
            
            if color == "red" and num > 12:
                can_play = False
                break
            if color == "blue" and num > 14:
                can_play = False
                break
            if color == "green" and num > 13:
                can_play = False
                break
    if can_play:
            total += game_id 
    
print(total)




