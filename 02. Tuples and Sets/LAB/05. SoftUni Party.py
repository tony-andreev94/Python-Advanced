# https://judge.softuni.bg/Contests/Practice/Index/1832#4


def missing_guests(reservations):
    guests = set()
    for _ in range(reservations):
        guests.add(input())

    command = input()
    while not command == "END":
        guests.remove(command)
        command = input()

    return guests


def print_missing_guests(guest_set):
    print(len(guest_set))
    guest_list = [each for each in guest_set]
    guest_list.sort()
    [print(guest) for guest in guest_list]


reservations = int(input())
print_missing_guests(missing_guests(reservations))
