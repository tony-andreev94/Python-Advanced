# https://judge.softuni.bg/Contests/Practice/Index/1838#1


def to_round(values):
    return [round(x) for x in values]


print(to_round(map(float, input().split())))
