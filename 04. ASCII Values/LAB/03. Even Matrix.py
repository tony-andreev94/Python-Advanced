# https://judge.softuni.bg/Contests/Practice/Index/1836#2

sublists = int(input())

# build matrix
matrix2 = [[int(x) for x in input().split(", ")] for _ in range(sublists)]
# remove odd numbers
print([[x for x in row if x % 2 == 0] for row in matrix2])

# no comprehensions
matrix = []
# build matrix
for _ in range(sublists):
    sublist = [int(x) for x in input().split(", ")]
    matrix.append(sublist)

# remove odds
for row in matrix:
    for element in row:
        if not element % 2 == 0:
            row.pop(row.index(element))

print(matrix)
