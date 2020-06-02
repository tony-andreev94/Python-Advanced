# https://judge.softuni.bg/Contests/Practice/Index/1832#2


def unique_names(number):
    names = set()
    # [names.add(input()) for _ in range(number)]   - with comprehension
    for _ in range(number):
        names.add(input())

    return names


def print_func(names_set):
    # [print(each) for each in names_set]    - with comprehension
    for each in names_set:
        print(each)


names_amount = int(input())
print_func(unique_names(names_amount))
