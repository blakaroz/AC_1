
with open("input.txt") as file:
    lines = file.readlines()
    print(lines)
    games_time = [int(time) for time in lines[0].split()[1:]]
    record_distances = [int(distance) for distance in lines[1].split()[1:]]
    games = list(zip(games_time,record_distances))
    

    ways_of_winning = []
    for game in games:
        game_time = game[0]
        record_distance = game[1]
        counter = 0
        for buttom_time in range(game_time):
            
            distance = buttom_time * (game_time - buttom_time)
            if distance > record_distance:
                counter +=1
        ways_of_winning.append(counter)

    ans = ways_of_winning[0] * ways_of_winning[1] * ways_of_winning[2] * ways_of_winning[3]
    print(counter)
    print(ways_of_winning)
    print(ans)


#this day was great - I was capable to do this part on my own

