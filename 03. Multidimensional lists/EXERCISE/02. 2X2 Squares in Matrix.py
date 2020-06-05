# https://judge.softuni.bg/Contests/Compete/Index/1835#1

matrix = []
(rows, columns) = [int(x) for x in input().split(" ")]
for _ in range(rows):
    row = input().split(" ")
    matrix.append(row)

matches = 0
for each_row in matrix:
    each_row_index = matrix.index(each_row)
    if each_row_index == len(matrix) - 1:
        break
    for index in range(len(each_row)):
        if index == columns - 1:
            break
        if each_row[index] == each_row[index + 1] == matrix[each_row_index + 1][index] == matrix[each_row_index + 1][index + 1]:
            matches += 1

print(matches)




