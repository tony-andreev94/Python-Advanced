# https://judge.softuni.bg/Contests/Compete/Index/1831#0


def reverse_func(stack):
    result = []
    while stack:
        result.append(stack.pop())

    return " ".join(result)


num_list = input().split(" ")
print(reverse_func(num_list))
