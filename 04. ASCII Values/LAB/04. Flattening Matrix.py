# https://judge.softuni.bg/Contests/Practice/Index/1836#3

sublists_amount = int(input())

# matrix = [input().split(", ") for _ in range(sublists_amount)]
matrix = []
for _ in range(sublists_amount):
    matrix.append(input().split(", "))


# flattened_matrix = [num for each_list in matrix for num in each_list]
flattened_matrix = []
for each_list in matrix:
    flattened_matrix += [int(num) for num in each_list]

print(flattened_matrix)
