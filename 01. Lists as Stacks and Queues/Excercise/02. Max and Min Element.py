# https://judge.softuni.bg/Contests/Compete/Index/1831#1
# 80/100


def query_func(n):
    stack = []
    result = []
    for i in range(n):
        command = input().split(" ")
        if int(command[0]) == 1:
            stack.append(int(command[1]))
        elif int(command[0]) == 2:
            if len(stack) > 0:
                stack.pop()
        elif int(command[0]) == 3:
            print(max(stack))
        elif int(command[0]) == 4:
            print(min(stack))
    while stack:
        result.append(str(stack.pop()))
    return ", ".join(result)


num = int(input())
print(query_func(num))
