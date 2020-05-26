# https://judge.softuni.bg/Contests/Practice/Index/1830#4
# 80/100
from collections import deque


def potato_func(kids_list, n):
    queue = deque(kids_list)
    index = 0
    while queue:
        queue.append(queue.popleft())
        index += 1
        if index == n:
            name = queue.pop()
            print(f"Removed {name}")
            index = 0
            if len(queue) == 1:
                print(f"Last is {queue.pop()}")
                break


kids = input().split(" ")
toss = int(input())

potato_func(kids, toss)
