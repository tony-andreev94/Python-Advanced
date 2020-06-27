# https://judge.softuni.bg/Contests/Compete/Index/2456#1
# 100/100 points
# TODO spaghetti code, to refactor the task


def in_field(tuple):
    if 0 <= tuple[0] < len(field) and 0 <= tuple[1] < len(field):
        return True


field_size = int(input())
field = []
burrow_position = []
for _ in range(field_size):
    row = input()
    field.append(row)
    if 'S' in row:
        snake_position = (field.index(row), row.index('S'))
    if 'B' in row:
        burrow_position.append((field.index(row), row.index('B')))

food_eaten = 0
cell_position = snake_position

while True:
    command = input()
    if command == "right":
        # move to new position
        cell_position = (snake_position[0], snake_position[1] + 1)
        row = cell_position[0]
        col = cell_position[1]
        if in_field(cell_position):
            if field[row][col] == '*':
                food_eaten += 1
            if field[row][col] == 'B':
                # print('true')
                # delete old S on field
                field[row] = field[row][:col - 1] + '.' + field[row][col:]
                # delete burrow entrance on field
                field[row] = field[row][:col] + '.' + field[row][col + 1:]
                # delete burrow entry in list and update snake position with other burrow
                del burrow_position[burrow_position.index(cell_position)]
                snake_position = burrow_position[0]
                # draw S on field
                field[snake_position[0]] = field[snake_position[0]][:snake_position[1]] + 'S' + field[snake_position[0]][snake_position[1] + 1:]
                # print(field[snake_position[0]])
            else:
                # delete old snake position
                field[row] = field[row][:col - 1] + '.' + field[row][col:]
                # draw S to new position
                field[row] = field[row][:col] + 'S' + field[row][col + 1:]
                snake_position = (row, col)
                if food_eaten == 10:
                    print("You won! You fed the snake.")
                    break
        else:
            field[row] = field[row][:col - 1] + '.' + field[row][col:]
            print("Game over!")
            break
    elif command == "left":
        # move to new position
        cell_position = (snake_position[0], snake_position[1] - 1)
        row = cell_position[0]
        col = cell_position[1]
        if in_field(cell_position):
            if field[row][col] == '*':
                food_eaten += 1
            if field[row][col] == 'B':   ###
                # print('true')
                # delete old S on field
                field[row] = field[row][:col + 1] + '.' + field[row][col + 2:]
                # delete burrow entrance on field
                field[row] = field[row][:col] + '.' + field[row][col + 1:]
                # delete burrow entry in list and update snake position with other burrow
                del burrow_position[burrow_position.index(cell_position)]
                snake_position = burrow_position[0]
                # draw S on field
                field[snake_position[0]] = field[snake_position[0]][:snake_position[1]] + 'S' + field[snake_position[0]][snake_position[1] + 1:]
                # print(field[snake_position[0]])
            else:
                # delete old snake position and draw new one
                field[row] = field[row][:col + 1] + '.' + field[row][col + 2:]
                field[row] = field[row][:col] + 'S' + field[row][col + 1:]
                snake_position = (row, col)
                if food_eaten == 10:
                    print("You won! You fed the snake.")
                    break
        else:
            field[row] = field[row][:col + 1] + '.' + field[row][col + 2:]
            print("Game over!")
            break

        pass
    elif command == "up":
        cell_position = (snake_position[0] - 1, snake_position[1])
        row = cell_position[0]
        col = cell_position[1]
        #######
        if in_field(cell_position):
            if field[row][col] == '*':
                food_eaten += 1
            if field[row][col] == 'B':
                # print('true')
                # delete old S on field
                field[row + 1] = field[row + 1][:col] + '.' + field[row + 1][col + 1:]
                # delete burrow entrance on field
                field[row] = field[row][:col] + '.' + field[row][col + 1:]
                # delete burrow entry in list and update snake position with other burrow
                del burrow_position[burrow_position.index(cell_position)]
                snake_position = burrow_position[0]
                # draw S on field
                field[snake_position[0]] = field[snake_position[0]][:snake_position[1]] + 'S' + field[snake_position[0]][snake_position[1] + 1:]
                # print(field[snake_position[0]])
            else:
                # delete old snake position and draw new one
                field[row + 1] = field[row + 1][:col] + '.' + field[row + 1][col + 1:]
                field[row] = field[row][:col] + 'S' + field[row][col + 1:]
                snake_position = (row, col)
                if food_eaten == 10:
                    print("You won! You fed the snake.")
                    break
        else:
            field[row + 1] = field[row + 1][:col] + '.' + field[row + 1][col + 1:]
            print("Game over!")
            break
        pass
    elif command == "down":
        cell_position = (snake_position[0] + 1, snake_position[1])
        row = cell_position[0]
        col = cell_position[1]
        if in_field(cell_position):
            if field[row][col] == '*':
                food_eaten += 1
            if field[row][col] == 'B':
                # print('true')
                # delete old S on field
                field[row - 1] = field[row - 1][:col] + '.' + field[row - 1][col + 1:]
                # delete burrow entrance on field
                field[row] = field[row][:col] + '.' + field[row][col + 1:]
                # delete burrow entry in list and update snake position with other burrow
                del burrow_position[burrow_position.index(cell_position)]
                snake_position = burrow_position[0]
                # draw S on field
                field[snake_position[0]] = field[snake_position[0]][:snake_position[1]] + 'S' + field[
                                                                                                    snake_position[0]][
                                                                                                snake_position[1] + 1:]
                # print(field[snake_position[0]])
            else:
                # delete old snake position and draw new one
                field[row - 1] = field[row - 1][:col] + '.' + field[row - 1][col + 1:]
                field[row] = field[row][:col] + 'S' + field[row][col + 1:]
                snake_position = (row, col)
                if food_eaten == 10:
                    print("You won! You fed the snake.")
                    break
        else:
            field[row - 1] = field[row - 1][:col] + '.' + field[row - 1][col + 1:]
            print("Game over!")
            break
    else:
        break

print(f"Food eaten: {food_eaten}")
for each in field:
    print(each)
