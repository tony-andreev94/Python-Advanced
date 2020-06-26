# https://judge.softuni.bg/Contests/Practice/Index/2025#0

expression = input().split()
temp_numbers = []
result = int(expression[0])
expression.pop(0)
for char in expression:
    if char == '+':
        for each_num in temp_numbers:
            result += each_num
        temp_numbers = []
    elif char == '-':
        for each_num in temp_numbers:
            result -= each_num
        temp_numbers = []
    elif char == '*':
        for each_num in temp_numbers:
            result *= each_num
        temp_numbers = []
    elif char == '/':
        for each_num in temp_numbers:
            result /= each_num
            result = int(result)
        temp_numbers = []
    else:
        temp_numbers.append(int(char))

print(result)
