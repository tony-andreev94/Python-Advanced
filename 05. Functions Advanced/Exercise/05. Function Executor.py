# https://judge.softuni.bg/Contests/Compete/Index/1839#4
# 0/100


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


def func_executor(*args):
    result = []
    for tuples in args:
        function = tuples[0]
        arguments = tuples[1]
        result.append(function(*arguments))

    return result

    # for index in range(len(args)):
    #     if args[index][0] == sum_numbers:
    #         result.append(sum_numbers(*args[index][1]))  # [0], args[index][1][1]))
    #     else:
    #         result.append(multiply_numbers(args[index][1][0], args[index][1][1]))
    #return result


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))
