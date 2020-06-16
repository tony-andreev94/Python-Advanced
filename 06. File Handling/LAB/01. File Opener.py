# Task 1

file_path = 'W:\\Documents\\@Python\\SoftUni\\python_advanced\\06_file_handling\\08-File-Handling-Lab-Resources\\File Opener\\text.txt'

try:
    open(file_path, 'r')
    print("File found")
except FileNotFoundError:
    print("File not found")
