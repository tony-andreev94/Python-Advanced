# https://judge.softuni.bg/Contests/Practice/Index/2306#2


def find_strongest_eggs(string, sublists):
    grid = []
    strong_eggs = []
    # build lists
    for _ in range(sublists):
        grid.append([])

    # populate lists
    i = 0
    for el in string:
        grid[i].append(el)
        i += 1
        if i == sublists:
            i = 0

    # find eggs
    mid_index = len(grid[0]) // 2
    for each_list in grid:
        number = each_list[mid_index]
        left_number = each_list[mid_index - 1]
        right_number = each_list[mid_index + 1]
        if left_number < number and right_number < number:
            if left_number < right_number:
                strong_eggs.append(number)

    return strong_eggs


# Testing
print(find_strongest_eggs([-1, 7, 3, 15, 2, 12], 2))
print(find_strongest_eggs([-1, 0, 2, 5, 2, 3], 2))
print(find_strongest_eggs([51, 21, 83, 52, 55], 1))
