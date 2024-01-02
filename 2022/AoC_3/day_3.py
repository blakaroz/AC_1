from string import ascii_lowercase, ascii_uppercase

with open("input.txt") as file:
    rucksacks = file.read().split("\n")


sum = 0
for rucksack in rucksacks:
    # print(len(rucksack))
    half = len(rucksack)//2
    pocket_1 = rucksack[half:]
    pocket_2 = rucksack[:half]
    # print(pocket_1,pocket_2)
    
    # same = pocket_1[i] in pocket_2[i]
    same = list(set(pocket_1) & set(pocket_2))
    # print(same)
    priority_dict = {char: i+1 for i,char in enumerate(ascii_lowercase)}
    priority_dict.update({char: i+27 for i,char in enumerate(ascii_uppercase)})
    value = priority_dict[same[0]] 
    sum += value
    
# print(ascii_uppercase)
# print(ascii_lowercase)
# print(priority_dict)
# print(value)
print(sum)


## part 2
sum2=0
#dla kazdego indexu od 0 do len of rucksack przeskakujac co trzy, slicuj te 3 elementy w array
groups = [rucksacks[i:i+3] for i in range(0,len(rucksacks),3)]
for group in groups:
    same = list(set(group[0]) & set(group[1]) & set(group[2]))
    value = priority_dict[same[0]]
    sum2 += value
    print(same)
print(sum2)