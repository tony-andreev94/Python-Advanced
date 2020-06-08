# https://judge.softuni.bg/Contests/Compete/Index/1837#4


def first_diagonal_sum(matrix):
    diagonal_sum = 0
    index = 0
    for each_row in matrix:
        diagonal_sum += int(each_row[index])
        index += 1
    return diagonal_sum


def first_diagonal_elements(matrix):
    index = 0
    elements = []
    for each_row in matrix:
        elements.append(each_row[index])
        index += 1
    return elements


def sec_diagonal_sum(matrix):
    diagonal_sum = 0
    index = len(matrix[0]) - 1
    for each_row in matrix:
        diagonal_sum += int(each_row[index])
        index -= 1

    return diagonal_sum


def sec_diagonal_elements(matrix):
    index = len(matrix[0]) - 1
    elements = []
    for each_row in matrix:
        elements.append(each_row[index])
        index -= 1
    return elements


# comprehension
size = int(input())
matrix = [input().split(", ") for _ in range(size)]
print(f"First diagonal: {', '.join(first_diagonal_elements(matrix))}. Sum: {first_diagonal_sum(matrix)}")
print(f"Second diagonal: {', '.join(sec_diagonal_elements(matrix))}. Sum: {sec_diagonal_sum(matrix)}")


# no comprehension

matrix = []
size = int(input())

for _ in range(size):
    matrix.append(input().split(", "))

print(f"First diagonal: {', '.join(first_diagonal_elements(matrix))}. Sum: {first_diagonal_sum(matrix)}")
print(f"Second diagonal: {', '.join(sec_diagonal_elements(matrix))}. Sum: {sec_diagonal_sum(matrix)}")
