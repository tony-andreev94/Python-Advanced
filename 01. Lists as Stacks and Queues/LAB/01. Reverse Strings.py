# https://judge.softuni.bg/Contests/Practice/Index/1830#0


def reverse_func(string):
    stack = list(string)
    result = ""
    while stack:
        char = stack.pop()
        result += char
    return result


text = input()
print(reverse_func(text))
