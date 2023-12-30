
total = 0

with open("data.txt") as file:
    for line in file:
        line = line.split(":")[1].strip() 
        winning_num, my_num = line.split(" | ")
        winning_num = set(winning_num.split())
        my_num = set(my_num.split())
    
        score = len(my_num & winning_num)
        if score > 0:
            total += 2 **(score-1)
    
    print(total)







# with open("data.txt") as file:
#     for x in file:
#         x = x.split(":")[1].strip()
#         winning_num, my_num = x.split("|")
#         winning_num = list(map(int,winning_num.split()))
#         my_num = list(map(int, my_num.split()))
       
#         score = sum(num in winning_num for num in my_num)
#         if score > 0:
#             total += 2 **(score-1)
# print(total)






# import re


# with open("data.txt") as file:
#     lines = file.read().strip().split("\n")


#     # print(lines)
#     ans = 0
#     for line in lines:
#         games = re.split("\s+",line)
#         winning_numbers = [int(num) for num in games[2:12]]
#         my_numbers = [int(num) for num in games[13:]]
        
#         score = 0
#         score = sum(num in my_numbers for num in winning_numbers)
#         # for num in my_numbers:
#         #     if num in winning_numbers:
#         #         score += 1
        
#         if score > 0:
#             ans += 2 ** (score-1)
#         # print(score)
#     print(ans)




