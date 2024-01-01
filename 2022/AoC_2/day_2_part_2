ROCK = "A"
PAPER = "B"
SCISSORS = "C"

LOSE_POINTS = 0
DRAW_POINTS = 3
WIN_POINTS = 6

LOSE = "X"
DRAW = "Y"
WIN = "Z"


with open("input_ex.txt") as file:
    lines = file.read().strip().split("\n")


def result_score(you,me):
    result = 0
    if you == me:
        result = DRAW_POINTS
    elif (you == ROCK and me == PAPER) or (you == PAPER and me == SCISSORS) or (you == SCISSORS and me == ROCK): 
        result = WIN_POINTS
    else:
        result = LOSE_POINTS
    return result


def shape_score(my_shape):
    score = {ROCK:1, PAPER:2, SCISSORS:3 }
    return score.get(my_shape)  


def choose_shape(you,me):
    shape_choice_win = {
        ROCK: PAPER,
        PAPER: SCISSORS,
        SCISSORS: ROCK
    }
    shape_choice_lose = {
        ROCK: SCISSORS,
        PAPER: ROCK,
        SCISSORS: PAPER
    }

    if me == DRAW:
       return you
    elif me == WIN:
        return shape_choice_win.get(you)
    else:
        return shape_choice_lose.get(you)


ans = 0

for line in lines:
    shape = line.split()
    you = shape[0]
    me = shape[1]

    me = choose_shape(you,me)

    ans += result_score(you, me) + shape_score(me)
    

print(ans)