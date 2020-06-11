# https://judge.softuni.bg/Contests/Practice/Index/1838#4


def min_max_sum_func(values):
    print(f"The minimum number is {min(values)}")
    print(f"The maximum number is {max(values)}")
    print(f"The sum number is: {sum(values)}")


min_max_sum_func(list(map(int, input().split())))
