from string import ascii_lowercase, ascii_uppercase

with open("input.txt") as file:
    rucksacks = file.read().split("\n")


total_sum = 0

priority_dict = {char: i+1 for i,char in enumerate(ascii_lowercase + ascii_uppercase)}



for rucksack in rucksacks:
    half = len(rucksack)//2
    pocket_1 = rucksack[half:]
    pocket_2 = rucksack[:half]
    
    same = list(set(pocket_1) & set(pocket_2))
    
    if same:
        total_sum += sum(priority_dict[char] for char in same)
    

print(total_sum)


### Part 2

total_sum_2 = 0

#dla kazdego indexu od 0 do len of rucksack przeskakujac co trzy, slicuj te 3 elementy w array
groups = [rucksacks[i:i+3] for i in range(0,len(rucksacks),3)]
for group in groups:
    same = list(set(group[0]) & set(group[1]) & set(group[2]))
    if same:
        total_sum_2 += sum(priority_dict[char] for char in same)


print(total_sum_2 ) 