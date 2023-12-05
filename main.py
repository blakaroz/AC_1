
with open("data.txt", "r") as file:
    data = file.read()

lines = data.split("\n")
print(lines)
sum_of_all_lines_numbers = 0

for line in lines:
    digits = []
    for digit in line:
        if digit.isdigit():
            digits.append(digit)
    sum_of_line = digits[0] + digits[-1]

    sum_of_all_lines_numbers += int(sum_of_line)
    
print(digits)
print(sum_of_line)
print(sum_of_all_lines_numbers)