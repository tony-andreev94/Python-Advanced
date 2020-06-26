# https://judge.softuni.bg/Contests/Practice/Index/2025#1


def is_in_field(cords_list):
    if 0 <= cords_list[0] < len(field) and 0 <= cords_list[1] < len(field):
        return True


directions = {'right': [0, 1],
              'left': [0, -1],
              'up': [-1, 0],
              'down': [1, 0]
              }

field_size = int(input())
field = []
total_targets = 0
plane_position = (0, 0)
for _ in range(field_size):
    row = input().split()
    field.append(row)
    for char in row:
        if char == 't':
            total_targets += 1
        elif char == 'p':
            plane_position = (field.index(row), row.index('p'))

current_targets = total_targets

commands_amount = int(input())
for _ in range(commands_amount):
    command_tokens = input().split()
    command = command_tokens[0]
    direction = command_tokens[1]
    steps = int(command_tokens[2])
    # logic:
    # get new cords/direction
    cell_position = [plane_position[0], plane_position[1]]
    for _ in range(steps):
        cell_position[0] += directions[direction][0]
        cell_position[1] += directions[direction][1]
    # check validity
    if is_in_field(cell_position):
        if command == 'shoot':
            if field[cell_position[0]][cell_position[1]] == 't':
                current_targets -= 1
            field[cell_position[0]][cell_position[1]] = 'x'
        elif command == 'move':
            if field[cell_position[0]][cell_position[1]] == '.':
                field[plane_position[0]][plane_position[1]] = '.'
                field[cell_position[0]][cell_position[1]] = 'p'
                plane_position = (cell_position[0], cell_position[1])


if current_targets == 0:
    print(f"Mission accomplished! All {total_targets} targets destroyed.")
elif current_targets > 0:
    print(f"Mission failed! {current_targets} targets left.")

for each in field:
    print(*each)
