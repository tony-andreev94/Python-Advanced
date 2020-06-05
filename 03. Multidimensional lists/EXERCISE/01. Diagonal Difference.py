# https://judge.softuni.bg/Contests/Compete/Index/1835#0


def build_matrix(matrix_size):
    matrix = []
    for _ in range(matrix_size):
        row = [int(x) for x in input().split(" ")]
        matrix.append(row)

    return matrix


def find_first_diagonal(matrix):
    diagonal_sum = 0
    index = 0
    for each_row in matrix:
        diagonal_sum += each_row[index]
        index += 1

    return diagonal_sum


def find_sec_diagonal(matrix):
    diagonal_sum = 0
    index = len(matrix[0]) - 1
    for each_row in matrix:
        diagonal_sum += each_row[index]
        index -= 1

    return diagonal_sum


matrix_size = int(input())
matrix = build_matrix(matrix_size)
first_diag = find_first_diagonal(matrix)
second_diag = find_sec_diagonal(matrix)

print(abs(first_diag - second_diag))
