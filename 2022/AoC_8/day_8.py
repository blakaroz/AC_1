with open("input_ex.txt") as file:
    trees = file.read().split("\n")


# trees = [trees]
print(trees)
print(trees[1])


zle bo musze wsyztkie spradzic w danym row/columnie czy ktores nie jesst wieksze a nie tylko sasiadow tylko cale row i cale column
sum = 0
# sum += len(trees[0]) *2
# for row in trees[1:-1]:
#     i = 0
#     sum +=2 # dodawanie dla kazdego row 1 drzewa

for row_i in range(len(trees)):
    if (row_i == 0 or row_i == len(row_i)-1):
        sum += len(trees[row_i])
    for column_i in range(len(trees[row_i])):
        current = trees[row_i][column_i]

        if column_i > 0 & column_i < len(trees[row_i])-1:
            left = trees[row_i][column_i-1]
            right = trees[row_i][column_i+1]
            up = trees[row_i-1][column_i]
            down = trees[row_i+1][column_i]
            if current > (left or right or up or down):
                sum +=1
    # # if index of column is first or last sum len of row
    #  if trees[row][collumn] = 0:
    #     sum += len(row)



print(sum)

