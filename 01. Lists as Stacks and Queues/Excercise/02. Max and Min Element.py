# https://judge.softuni.bg/Contests/Compete/Index/1831#1


def query_func(n):
    stack = []
    for _ in range(n):
        command_input = input().split(" ")
        command = int(command_input[0])
        if command == 1:
            stack.append(int(command_input[1]))
        elif command == 2 and stack:  # check if stack is empty before pop()
            stack.pop()
        elif command == 3 and stack:  # check if stack is empty before using min()/max()
            print(max(stack))
        elif command == 4 and stack:
            print(min(stack))

    return ", ".join([str(el) for el in reversed(stack)])


num = int(input())
print(query_func(num))
