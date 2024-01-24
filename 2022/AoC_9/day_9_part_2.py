
# Nie zrobione  - coś źle od punktu lini 32

with open("input_ex.txt") as file:
    movements = file.read().split("\n")

# print(movements)

# set of values - first saart wiuth coor 0,0 so they are inicializace
counter = set([(0,0)])

R = [[0,0] for _ in range(10)]
# print(R)
for line in movements:
    direction, how_many = line.split()
    how_many = int(how_many)
    # print(line)

    # dla kazdejgo i w rangu how many:
    for _ in range(how_many):
        # 1 jesli r lub - 1 jesli l, else = 0czyli nie ruszaj x
        direction_x = 1 if direction == "R" else -1 if direction == "L" else 0
        #  dir y = 1 jesli down -1 jesli up else 0 czyli nie ruszaj y
        direction_y = 1 if direction == "U" else -1 if direction == "D" else 0

        # R [0] czyli head - rusz go o 1 lub -1 a potem kazdy kolejny element zmien koordynaty
        R[0][0] += direction_x
        R[0][1] += direction_y

        # print(R[0])
        # moving the tail
        for i in range(9):
            # head to bieący el. rope a T to kolejny element z rope
            H = R[i]
            T = R[i+1]
            
     
            distance_x = H[0] - T[0]
            distance_y = H[1] - T[1]

            if abs(distance_x) > 1 or abs(distance_y) > 1:
                if distance_x == 0:
                    T[1] += 1 if distance_y > 0 else -1
                elif distance_y == 0:
                    T[0] += 1 if distance_x > 0 else -1
                else:
                    T[0] += 1 if distance_x > 0 else -1
                    T[1] += 1 if distance_y > 0 else -1
                # add tail
        print(H)
        print(T)
         
        
#     counter.add(tuple(R[-1]))

# print(len(counter))
        # move tail if distans is further that 1 (abs value czyli czy wiekszy niz 1 w lwewo czyli -1 czy w prawo czyli +1)
            # jesli move  w tym samym row czyli 0 lub tej samej columnie czyli col 0 to tail te 0+1
            # 
        # dodaj coordinaty do array with values where it is