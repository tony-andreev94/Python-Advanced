# https://judge.softuni.bg/Contests/Practice/Index/1830#1


def find_exp(data):
    stack = []
    result = []

    for index in range(len(data)):
        char = data[index]
        if char == "(":
            stack.append(index)
        elif char == ")":
            start_index = stack.pop()
            result.append(data[start_index:index + 1])
    return result


expression = input()
for each in find_exp(expression):
    print(each)
