# Task 2

file_path = 'W:\\Documents\\@Python\\SoftUni\\python_advanced\\06_file_handling\\08-File-Handling-Lab-Resources\\File Reader\\numbers.txt'

with open(file_path, 'r') as file:
    numbers_sum = 0
    while True:
        number = file.readline()
        if number == '':
            print(numbers_sum)
            break
        else:
            numbers_sum += int(number)
