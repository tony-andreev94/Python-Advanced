# https://judge.softuni.bg/Contests/Practice/Index/1838#2


def find_even_n(values):
    return [x for x in values if x % 2 == 0]


print(find_even_n(map(int, input().split())))
