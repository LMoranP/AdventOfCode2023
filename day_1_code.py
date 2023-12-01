import re
# Reading the input
text = open("Path/AdventOfCode2023/day_1_input.txt", "r")

num_list = list([])
for line in text.readlines():

    # Obtaining first digit
    first_number = re.search(r'\d+', line)[0][0]

    # Obtaining last digit
    last_number = re.search(r'(?:\d+)(?!.*\d)', line)[0][-1]

    # Creating the concatenation digit
    generated_num = int(str(first_number) + str(last_number))

    # Appending the digit to the empty list
    num_list.append(generated_num)

# Summing all the digits in the list
print(sum(num_list))