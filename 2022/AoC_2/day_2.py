# x - rock
# y - paper
# z - scissors

LOSE_POINTS = 0
DRAW_POINTS = 3
WIN_POINTS = 6

#changing keys to be equal to compare result from games easier
replacement_dic = {"A":"X", "B":"Y", "C":"Z"}

with open("input.txt") as file:
    lines = file.read().strip().split("\n")


def result_score(you,me):
    
    if you == me:
        return DRAW_POINTS
    elif (you == "X" and me == "Y") or (you == "Y" and me == "Z") or (you == "Z" and me == "X"): 
        return WIN_POINTS
    else:
        return LOSE_POINTS


def shape_score(my_shape):
    score = {"X":1, "Y":2, "Z":3 }
    return score.get(my_shape)  


ans = 0

for line in lines:
    choice = line.split()
    you = replacement_dic.get(choice[0])
    me = choice[1]
    ans += result_score(you, me) + shape_score(me)
    
print(ans)