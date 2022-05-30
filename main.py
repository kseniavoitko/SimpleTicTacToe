import math

count_of_move = 1


def print_grid(grid):
    print('---------')
    print(f'| {" ".join(grid[0])} |')
    print(f'| {" ".join(grid[1])} |')
    print(f'| {" ".join(grid[2])} |')
    print('---------')


def make_a_move():
    global count_of_move
    move = input("Make a move: ").split()
    try:
        move = [int(x) for x in move]
    except ValueError:
        print('You should enter numbers!')
        make_a_move()
        return

    player = 'X' if count_of_move % 2 == 1 else 'O'
    x = move[0] - 1
    y = move[1] - 1

    try:
        if grid[x][y] != ' ':
            print('This cell is occupied! Choose another one!')
            make_a_move()
            return
        grid[x][y] = player
    except IndexError:
        print('Coordinates should be from 1 to 3!')
        make_a_move()
        return

    count_of_move += 1


def analise_grid(grid):
    for raw in range(3):
        if grid[raw][0] == grid[raw][1] == grid[raw][2] != ' ':
            return f'{grid[raw][0]} wins'
    for column in range(3):
        if grid[0][column] == grid[1][column] == grid[2][column] != ' ':
            return f'{grid[0][column]} wins'
    if grid[0][0] == grid[1][1] == grid[2][2] != ' ' \
            or grid[0][2] == grid[1][1] == grid[2][0] != ' ':  # check diagonals
        return f'{grid[1][1]} wins'
    empty_cells = [cell for row in grid for cell in row if cell == ' ']
    if len(empty_cells) == 0:
        return 'Draw'
    return ''


grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
print_grid(grid)
the_end = False
while not the_end:
    make_a_move()
    print_grid(grid)
    the_end = analise_grid(grid)
print(the_end)
