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

    # if it was necessary to first print the ones with letters, and then the ones with digits:
    # [print(guest) for guest in guest_set if not guest[0].isdigit()]  # first print the ones starting with letter
    # [print(guest) for guest in guest_set if guest[0].isdigit()]  # then print the ones starting with digit


reservations = int(input())
print_missing_guests(missing_guests(reservations))
