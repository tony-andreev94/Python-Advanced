# https://judge.softuni.bg/Contests/Compete/Index/1839#1


def find_sum(command, values):
    if command == "Odd":
        return sum([x for x in values if not x % 2 == 0]) * len(values)
    elif command == "Even":
        return sum([x for x in values if x % 2 == 0]) * len(values)


command = input()
values_list = [int(x) for x in input().split()]
print(find_sum(command, values_list))
