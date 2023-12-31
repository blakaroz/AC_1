# a - rock
# b - paper
# c - sciccors

# x - rock
# y - paper
# x - scissors

# scores: scores for shape selected + outco of rounf
# shapes
# 1- rock
# 2 - paper 
# 3 - scissors
# output:
# o - lost
# 3 - Drow
# 6 - won

with open("input_ex.txt") as file:
    games = file.read().split("\n")



print(games)
