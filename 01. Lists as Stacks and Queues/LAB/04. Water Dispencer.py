# https://judge.softuni.bg/Contests/Practice/Index/1830#3
from collections import deque

water_quantity = int(input())
queue = deque()

while True:
    command = input()
    if command == "Start":
        break
    else:
        queue.append(command)

while True:
    command = input().split(" ")
    if command[0] == "End":
        print(f"{water_quantity} liters left")
        break
    elif command[0] == "refill":
        water_quantity += int(command[1])
    else:
        needed_water = int(command[0])
        if needed_water <= water_quantity:
            person_name = queue.popleft()
            print(f"{person_name} got water")
            water_quantity -= needed_water
        else:
            person_name = queue.popleft()
            print(f"{person_name} must wait")
