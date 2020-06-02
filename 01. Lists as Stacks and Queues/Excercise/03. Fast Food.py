# https://judge.softuni.bg/Contests/Compete/Index/1831#2
from collections import deque


def check_food(food_quantity):
    orders_left = []
    queue = deque([int(x) for x in input().split(" ")])
    biggest_order = max(queue)
    print(biggest_order)

    while queue:
        order = queue.popleft()
        if order <= food_quantity:
            food_quantity -= order
        else:
            orders_left.append(str(order))

    if len(orders_left) == 0:
        return "Orders complete"
    else:
        return f"Orders left: {' '.join(orders_left)}"


quantity = int(input())
print(check_food(quantity))
