# https://judge.softuni.bg/Contests/Compete/Index/2456#2


def list_manipulator(input_list, *args):
    action = args[0]
    place = args[1]
    numbers = [*args]
    numbers.pop(0)
    numbers.pop(0)

    if action == 'remove':
        if len(numbers) > 0:
            boundary = numbers[0]
        else:
            boundary = 1
        for _ in range(int(boundary)):
            if place == 'beginning':
                input_list.pop(0)
            elif place == 'end':
                input_list.pop()

    elif action == 'add':
        if place == 'beginning':
            for each_number in numbers[::-1]:
                input_list.insert(0, each_number)
        elif place == 'end':
            for each_number in numbers:
                input_list.append(each_number)

    return input_list


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
