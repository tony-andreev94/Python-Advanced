# https://judge.softuni.bg/Contests/Compete/Index/1837#6

result = [el for el in [each.split() for each in input().split("|")]][::-1]

for each_row in result:
    for element in each_row:
        print(element, end=" ")


# no comprehension
result = []
string = input().split("|")

for each in string:
    row = each.split()
    result.append(row)

for each_row in result[::-1]:
    for element in each_row:
        print(element, end=" ")


