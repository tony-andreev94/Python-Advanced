# https://judge.softuni.bg/Contests/Compete/Index/1833#1
# redo and make a return instead of print?


def find_elements(a, b):
    first_l = []
    second_l = []
    for i in range(a):
        el = int(input())
        first_l.append(el)

    for i in range(b):
        el = int(input())
        second_l.append(el)

    first_set = set(first_l)
    second_set = set(second_l)

    for each in first_set:
        if each in second_set:
            print(each)


user_input = input().split(" ")
find_elements(int(user_input[0]), int(user_input[1]))
