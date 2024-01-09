with open("input_ex.txt") as file:
    lines = file.read().split("\n")

 
operation_dict = {"move": [], "from": [], "to": []}

for line in lines:
    # print(line)
    move, how_many, froom, where_from, to, where_to = line.split()
    operation_dict["move"].append(how_many)
    operation_dict["from"].append(where_from)
    operation_dict["to"].append(where_to)
    
# print(operation_dict)

conteners_dict_no = [["Z", "N"],["M", "C", "D"],["P"]]

conteners_dict = [["F","T","C","L","R","P","G","Q"],
    ["N","Q","H","W","R","F","S","J"],
    ["F","B","H","W","P","M","Q"],
    ["V","S","T","D","F"],
    ["Q","L","D","W","V","F","Z"],
    ["Z","C","L","S"],
    ["Z","B","M","V","D","F"],
    ["T","J","B"],
    ["Q","N","B","G","L","S","P","H"]]


# print(conteners_dict)

for i in range(len(operation_dict["move"])):
    where_from = int(operation_dict["from"][i]) - 1
    how_many = int(operation_dict["move"][i])
    where_to = int(operation_dict["to"][i]) - 1



#Part 1
    # for box in range(how_many):
    #     print(box)
    #     remove = conteners_dict[where_from].pop()
    #     conteners_dict[where_to].append(remove)

#Part 2
    # for box in range(how_many):
    remove = conteners_dict[where_from][-how_many:]
    
    conteners_dict[where_from] = conteners_dict[where_from][:-how_many]
    conteners_dict[where_to].extend(remove)
   


# print(conteners_dict)


ans = ""
for container in conteners_dict:
    if container:  
        ans += container[-1]
print(ans)


# print(conteners_dict)


