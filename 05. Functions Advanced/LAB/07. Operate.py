# https://judge.softuni.bg/Contests/Practice/Index/1838#6


def operate(operator, *args):
    if operator == "+":
        return add(*args)
    elif operator == "-":
        return subtract(*args)
    elif operator == "*":
        return multiply(*args)
    elif operator == "/":
        return divide(*args)


def add(*args):
    return sum(args)


def subtract(*args):
    result = 0
    for arg in args:
        result -= arg
    return result


def multiply(*args):
    if len(args) == 0:
        return 0
    else:
        result = 1
        for arg in args:
            result *= arg
        return result


def divide(*args):
    if len(args) == 0:
        return 0
    else:
        result = 1
        for arg in args:
            result /= arg
        return result


print(operate("+", 1, 2, 0))
print(operate("*"))
print(operate("-", 1, 2, 4))
print(operate("/", 1))
