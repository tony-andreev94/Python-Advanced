# Task 4

from os import remove

file_path = "W:\\Documents\\@Python\\SoftUni\\python_advanced\\06_file_handling\\demos\\my_first_file.txt"

try:
    remove(file_path)
except FileNotFoundError:
    print(f'File already deleted!')
