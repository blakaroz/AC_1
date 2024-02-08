with open("input_on.txt") as file:
    parts = [x for x in file.read().strip().split("\n\n")]
# print(parts)
parts = [part.split("\n") for part in parts]

def compare(left,right):
    if type(left) == int:
        if type(right) == int:
            return left - right
        if type(right) == list:
            return compare([left], right)
    else:
        if type(right) == int:
            return compare(left, [right])
    
    for l,r in zip(left,right):
        result = compare(l,r)
        if result: #if result not 0 so false than
            return result # return value but care only about sign becouse if it will be minus its sign that is right order
        
    #lastly if nothing from above wasnt return is sign that some is shorten than other so again we will check the sign
    return len(left) - len(right) #if (-) its right order

ans = 0

for i, (left,right) in enumerate(parts):
    # print(i, (left,right))
    if compare(eval(left),eval(right)) < 0:
        ans += i + 1 

print(ans)

