with open("input_ex.txt") as file:
    movements = file.read().split("\n")

print(movements)

# set of values - first saart wiuth coor 0,0 so they are inicializace
counter = set([(0,0)])

H = [0,0]
T = [0,0]

for line in movements:
    direction, how_many = line.split()
    how_many = int(how_many)
    print(line)

    # dla kazdejgo i w rangu how many:
    for _ in range(how_many):
        direction_x = 1 jesli r lub - 1 jesli l, else = czyli nie ruszaj x
        direction_y = dir y = 1 jesli down -1 jesli up else 0 czyli nie ruszaj y
    
        # h[0] czli miejsce pierwsze czyli x czyli row += dx
        # h[1] czyli po columnie czyli gora dol += dy
        H[0] += direction_x
        H[1] += direction_y

        # CHECK DIFERENCES  for x and y miedzy h i t
        if h directiony abs difercn x >1 or abs y > 1 (zawsze chekujemy jak iwecej o 1 czyli juz 2 dzialamy a nie czkeamy do konca akcji )
            # jesli zmian 0 jest 0 to czyli musimy zmienic tylko y, jesli y 0 to zmienic tylko x O TE ROZNICE ABS O X LUB Y i jesli dif jest plus to t[x or y] +1 a jesli difr < 0 to t[x or y] -1
            #  else jesli nie sa w tym samym row or column musimy isc diagonalnie:  
                # to i t[0] czyli x zmieniamy i to[1] czyli y zmienaimy o diff
        counter.add(t coord)

    # move tail if distans is further that 1 (abs value czyli czy wiekszy niz 1 w lwewo czyli -1 czy w prawo czyli +1)
        # jesli move  w tym samym row czyli 0 lub tej samej columnie czyli col 0 to tail te 0+1
        # 
    # dodaj coordinaty do array with values where it is