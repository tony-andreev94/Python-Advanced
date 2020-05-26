# https://judge.softuni.bg/Contests/Compete/Index/1831#3


def organize_clothes(clothes_value, rack_capacity):
    racks = 1
    stack = clothes_value
    current_clothes = 0
    while stack:
        clothes_amount = int(stack.pop())
        if current_clothes + clothes_amount <= rack_capacity:
            current_clothes += clothes_amount
        else:
            racks += 1
            current_clothes = clothes_amount

    return racks


clothes = input().split(" ")
rack_capacity = int(input())

print(organize_clothes(clothes, rack_capacity))
