# https://judge.softuni.bg/Contests/Practice/Index/1834#0
# amount of columns is not needed, but it's given as input


def build_matrix(rows, columns):
    matrix = []
    for _ in range(int(rows)):
        row = [int(x) for x in input().split(", ")]
        matrix.append(row)
    return matrix


def find_sum(matrix):
    matrix_sum = 0
    for each_row in matrix:
        matrix_sum += sum(each_row)

    return matrix_sum


def print_result(matrix, matrix_sum):
    print(matrix_sum)
    print(matrix)


(rows, columns) = [int(x) for x in input().split(", ")]

matrix = build_matrix(rows, columns)
element_sum = find_sum(matrix)
print_result(matrix, element_sum)
