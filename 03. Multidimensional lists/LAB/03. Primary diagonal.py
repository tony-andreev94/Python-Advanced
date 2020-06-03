# https://judge.softuni.bg/Contests/Practice/Index/1834#1


def build_matrix(matrix_size):
    matrix = []
    for _ in range(matrix_size):
        row = [int(x) for x in input().split(" ")]
        matrix.append(row)

    return matrix


def find_diagonal_sum(matrix):
    diagonal_sum = 0
    index = 0
    for each_row in matrix:
        diagonal_sum += each_row[index]
        index += 1

    return diagonal_sum


matrix_size = int(input())
print(find_diagonal_sum(build_matrix(matrix_size)))
