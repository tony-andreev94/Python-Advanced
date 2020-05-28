# https://judge.softuni.bg/Contests/Compete/Index/1833#2
# redo and make a return instead of print?


def find_unique_elements(num):
    elements_list = []
    for i in range(num):
        user_input = input().split(" ")
        elements_list.extend(user_input)

    for each in set(elements_list):
        print(each)


num = int(input())
find_unique_elements(num)
