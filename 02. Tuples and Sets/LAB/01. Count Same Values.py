# https://judge.softuni.bg/Contests/Practice/Index/1832#0


def count_values(user_values):
    values_count = {}

    for value in user_values:
        if value not in values_count:
            values_count[value] = 0
        values_count[value] += 1

    return values_count


def print_values(values_dict):
    for (value, count) in values_dict.items():
        print(f"{float(value)} - {count} times")


user_values = input().split(" ")
print_values(count_values(user_values))
