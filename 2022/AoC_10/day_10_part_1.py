with open("input_ex.txt") as file:
    lines = file.read().split("\n")
# print(lines)


x = 1
database = [0]

for line in lines:
    if line == "noop":
        database.append(x)
    else:
        value = int(line.split()[1])
        database.append(x)
        database.append(x)
        x += value

database.append(x)


# enumerate musi byc skonwertowane do listy bo inaczej jest obiektem i dodatkowo slicuje zeby uzyskac tylko dla mnie wartosciowe indeksy

# i potem copehension list do uzyskania sumy mnozenia tych wartosci we wszytkich przypadkach
ans = sum(x*y for x,y in list(enumerate(database))[20::40])
print(ans)

