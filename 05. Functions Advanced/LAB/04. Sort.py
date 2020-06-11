# https://judge.softuni.bg/Contests/Practice/Index/1838#3


def sort_func(values):
    return sorted(values)


print(sort_func(map(int, input().split())))
print(sorted([int(x) for x in input().split()]))
