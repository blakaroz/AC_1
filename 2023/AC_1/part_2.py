with open("data.txt", "r") as file:
    data = file.read()

dictionary_of_digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

lines = data.split("\n")
print(lines)

sum_of_all_lines_numbers = 0

for line in lines:
    digits = []
    # check if any char is a digit
    for i,c in enumerate(line):
        if c.isdigit():
            digits.append(c)
        # check if any splot of char in line cover digit as word
        for key in dictionary_of_digits:
            if line[i:].startswith(key):
                digits.append(dictionary_of_digits[key])
    sum_of_line = int(digits[0] + digits [-1])
    sum_of_all_lines_numbers += sum_of_line 

print(lines)
print(sum_of_all_lines_numbers)