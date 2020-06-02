# https://judge.softuni.bg/Contests/Practice/Index/1832#2


def unique_names(number):
    # names = set()
    # [names.add(input()) for _ in range(number)] # list comprehension
    names = {input() for _ in range(number)}  # set comprehension

    return names


def print_func(names_set):
    [print(each) for each in names_set]


names_amount = int(input())
print_func(unique_names(names_amount))
