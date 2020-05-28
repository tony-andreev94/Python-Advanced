# https://judge.softuni.bg/Contests/Compete/Index/1833#3
# redo and find a smarter way to sort the set


def symbol_count(string):
    elements = []
    unique_list = []
    for each in string:
        elements.append(each)

    # remove duplicates
    unique = set(elements)

    # sort elements
    for each in unique:
        unique_list.append(each)
    unique_list.sort()

    for each in unique_list:
        print(f"{each}: {elements.count(each)} time/s")


string = input()
symbol_count(string)
