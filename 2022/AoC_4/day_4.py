with open("input_ex.txt") as file:
    data = file.read().split("\n")


lines = [lines.split(',') for lines in data]
# print(lines)
data_with_ranges = []

# Converting string pairs into range of numbers
for pairs in lines:
    pairs_ranges = []
    for pair in pairs:
        start, end = pair.split("-")
        pairs_ranges.append(range(int(start),int(end) +1))

    # print(pairs_ranges)
    data_with_ranges.append(pairs_ranges)


print(data_with_ranges)

sum1 = 0
sum2 = 0
for pairs in data_with_ranges:
    print(pairs)
    
    section1 = set(pairs[0])
    section2 = set(pairs[1])
    if section1.issubset(section2) or section2.issubset(section1):
            sum1+=1
    if section1.intersection(section2):
         sum2 +=1
         

print(sum1)
print(sum2)
