# https://judge.softuni.bg/Contests/Practice/Index/1834#1
# amount of columns is not needed, but it's given as input

def build_matrix(rows_amount, columns):
    matrix = []
    for _ in range(rows_amount):
        row = [int(x) for x in input().split(" ")]
        matrix.append(row)

    return matrix


def find_sum(matrix):
    for i in range(len(matrix[0])):
        column_sum = 0
        for each in matrix:
            column_sum += each[i]
        print(column_sum)


# Alternative solution:
def find_sum2(matrix):
    columns_sum = [0] * columns_count
    for row in range(rows_count):
        for column in range(columns_count):
            columns_sum[column] += matrix[row][column]

    # Print result:
    [print(each_sum) for each_sum in columns_sum]


(rows_count, columns_count) = [int(x) for x in input().split(", ")]

find_sum(build_matrix(rows_count, columns_count))
# find_sum2(build_matrix(rows_count, columns_count))
