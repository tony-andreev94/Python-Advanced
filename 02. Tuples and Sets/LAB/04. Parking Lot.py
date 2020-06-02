# https://judge.softuni.bg/Contests/Practice/Index/1832#3


def parking_lot(number):
    cars = set()
    for _ in range(number):
        (direction, car_plate) = input().split(", ")  # unpacking example
        if direction == "IN":
            cars.add(car_plate)
        elif direction == "OUT":
            if car_plate in cars:
                cars.remove(car_plate)

    return cars


def print_cars(cars):
    if cars:
        [print(each) for each in cars]
    else:
        print("Parking Lot is Empty")


commands = int(input())
print_cars(parking_lot(commands))
