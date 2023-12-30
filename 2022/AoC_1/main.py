# 1. otworz plik i czytaj go jako array wtih separated value
# według (/n) ale jakby nested bo muszą byc wszystkie a podzieli je luka

with open("input.txt") as file:
    groups = file.read().split("\n\n")


# for group in groups => map (ze string -> int, na podgrupach, które będą splitowane po nowych liniach)
# z tego zrób nested list array
data = [list(map(int, group.split('\n'))) for group in groups]

# poprzednia easy wersja:

# max_sum = 0 
# for group in data:
#     sum = 0
#     for num in group:
#         sum += num
#     if sum > max_sum:
#         max_sum = sum

# For group in data -> suma kadej grupy. Wybierz max sume szukając po sumach danych grup.
max_sum = max(sum(group) for group in data)
print(max_sum)


# Part 2

sums = list(sum(group) for group in data)


def sum_of_maxs(sums):
    maxs = []
    for _ in range(3):
        find_max = max(sums)
        maxs.append(find_max)
        sums.remove(find_max)

    sum_of_maxs = sum(maxs)
    return sum_of_maxs
    
print(sums)
print(sum_of_maxs(sums))


