dict = {1: ["N", "Z"],
        2: ["M", "C", "D","F"],
        3: ["P"]}

print(dict)

remove = dict[2][-2:]
dict[2] = dict[2][:-2]
dict[3].extend(remove)
print(remove)
print(dict[2])

print(dict)

string = ""
for value in dict.values():
    string += value[-1]
print(string)
