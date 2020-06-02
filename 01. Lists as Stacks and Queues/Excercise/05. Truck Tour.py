# https://judge.softuni.bg/Contests/Compete/Index/1831#4
from collections import deque


def pump_func(n):
    pumps = deque()
    original_pumps = []  # used for recursion, always revert to original deque if it fails on 1st,2nd.. etc. iteration
    fuel = 0
    for _ in range(n):
        tokens = [int(x) for x in input().split(" ")]
        pumps.append(tokens)
        original_pumps.append(tokens)

    for i in range(n):
        pumps.rotate(-i)
        current = pumps.popleft()
        while pumps:  # loop through petrol pumps
            fuel += current[0]
            if fuel >= current[1]:  # if trip is successful remove the pump
                fuel -= current[1]
                current = pumps.popleft()
            else:  # if trip fails revert to original deque and 0 fuel and start over
                fuel = 0
                pumps = deque(original_pumps[:])
                break

        if not pumps:  # if the while loop ended and deque is empty trip is successful
            return i


petrol_pumps = int(input())
print(pump_func(petrol_pumps))
