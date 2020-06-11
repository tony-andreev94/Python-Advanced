# https://judge.softuni.bg/Contests/Practice/Index/1838#0


def to_abs(values):
    return [abs(x) for x in values]


print(to_abs(map(float, input().split())))
