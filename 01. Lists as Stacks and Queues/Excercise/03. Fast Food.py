# https://judge.softuni.bg/Contests/Compete/Index/1831#2
# 80/100
from collections import deque


def check_food(food_quantity):
    orders_left = []
    queue = deque(input().split(" "))
    biggest_order = 0

    while queue:
        order = int(queue.popleft())
        if order > biggest_order:
            biggest_order = order
        if order <= food_quantity:
            food_quantity -= order
        else:
            orders_left.append(str(order))

    print(biggest_order)
    if len(orders_left) == 0:
        return "Orders complete"
    else:
        return f"Orders left: {' '.join(orders_left)}"


quantity = int(input())
print(check_food(quantity))
