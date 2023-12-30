with open("input.txt") as file:
    lines = file.readlines()
   
    game_time = int(lines[0].strip().replace(" ","").split(":")[1])
    record_distance = int(lines[1].strip().replace(" ","").split(":")[1])

    
    counter = 0
    for buttom_time in range(game_time):
        
        distance = buttom_time * (game_time - buttom_time)
        if distance > record_distance:
            counter +=1
    
    print(counter)