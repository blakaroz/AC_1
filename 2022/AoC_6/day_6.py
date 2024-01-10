with open("input_ex.txt") as file:
    data=file.read()

print(data)

i = 0
found = False
while not found:

    for i in range(len(data)):
        chars_box = data[i:i+14]
        #check if next 4 chars are different
        if len(chars_box) == len(set(chars_box)):
            print(chars_box)
            idx = data.find(chars_box) +14
            print(idx)
            found = True
            break
               
