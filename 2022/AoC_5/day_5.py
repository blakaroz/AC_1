with open("input_ex.txt") as file:
    lines = file.read().split("\n")

# print(data)

# lines = [line.split(",") for line in data]
# print(lines)

# from input lines set conteners_dict with will look like:
# {move: 1,3,2,1,
# from: 2,1,2,1,
# to:1,3,1,2}  
operation_dict = {"move": [], "from": [], "to": []}

for line in lines:
    print(line)
    move, how_many, froom, where_from, to, where_to = line.split()
    operation_dict["move"].append(how_many)
    operation_dict["from"].append(where_from)
    operation_dict["to"].append(where_to)
    
print(operation_dict)

conteners_dict = {1: ["N", "Z"],
        2: ["M", "C", "D"],
        3: ["P"]}

# print(conteners_dict)
for i in range(len(operation_dict["move"])):
    where_from = int(operation_dict["from"][i])
    how_many = int(operation_dict["move"][i])
    where_to = int(operation_dict["to"][i])

    if how_many <= len(conteners_dict[where_from]):
        remove = conteners_dict[where_from][-how_many:]
        conteners_dict[where_from] = conteners_dict[where_from][:-how_many]
        conteners_dict[where_to].extend(remove)
print(conteners_dict)


ans = ""
for value in conteners_dict.values():
    ans += value[-1]
print(ans)
