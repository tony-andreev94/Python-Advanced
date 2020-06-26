# https://judge.softuni.bg/Contests/Practice/Index/2306#1


def is_valid(cell_position):
    if 0 <= cell_position[0] < len(field) and 0 <= cell_position[1] < len(field):
        return True


field_size = int(input())
field = []

for i in range(field_size):
    row = input().split()
    field.append(row)
    if "B" in row:
        bunny_pos = (field.index(row), row.index('B'))

directions = {"right": [0, 1],
              "left": [0, -1],
              "down": [1, 0],
              "up": [-1, 0]
              }

eggs_collected = {'right': 0,
                  'left': 0,
                  'down': 0,
                  'up': 0
                  }

cell_steps = {'right': [],
              'left': [],
              'down': [],
              'up': []
              }

best_direction = 'right'


for each_direction in directions:
    row = bunny_pos[0]
    col = bunny_pos[1]
    current_position = [row, col]
    while is_valid(current_position):
        cell = field[current_position[0]][current_position[1]]
        if cell == 'X':
            break
        elif cell == 'B':
            pass
        else:
            eggs_collected[each_direction] += int(cell)
            cell_steps[each_direction].append([current_position[0], current_position[1]])
        current_position[0] += directions[each_direction][0]
        current_position[1] += directions[each_direction][1]
        if eggs_collected[each_direction] > eggs_collected[best_direction]:
            best_direction = each_direction


print(best_direction)
for each in cell_steps[best_direction]:
    print(each)
print(eggs_collected[best_direction])

