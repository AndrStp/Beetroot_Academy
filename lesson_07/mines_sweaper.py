from random import randint


MINES = 10
MAX_ROWS = 8
MAX_COLS = 8
MINED = -1

mines = set()
while len(mines) != MINES:
    x, y = randint(0, MAX_ROWS - 1), randint(0, MAX_COLS - 1)
    mines.add((x, y))

print('mines:', mines)

grid = [
    [-1 if (i, j) in mines else 0
     for j in range(MAX_COLS)]
    for i in range(MAX_ROWS)
]


for x, y in mines:
    possible_x = [i for i in range(x - 1, x + 2) if 0 <= i < MAX_ROWS]
    possible_y = [j for j in range(y - 1, y + 2) if 0 <= j < MAX_COLS]
    neighbours = [(x2, y2) for x2 in possible_x for y2 in possible_y]
    neighbours.remove((x, y))
    for row, col in neighbours:
        if grid[row][col] != -1:
            grid[row][col] += 1

# technical print, to see all bombs
for i in grid:
    for it in i:
        print(it if it == -1 else " " + str(it), end='  ')
    print()

for i in range(MAX_ROWS):
    for j in range(MAX_COLS):
        print('X', end=' ')
    print()

user_session = dict()

while len(user_session) != MAX_COLS * MAX_ROWS - MINES:
    user_input = input('Give me coordinates in format row col: ')
    row, col = user_input.split()
    row, col = int(row), int(col)

    if grid[row][col] == MINED:
        print('Sorry you have lost')
        break
    else:
        user_session[(row, col)] = True

    for i in range(MAX_ROWS):
        for j in range(MAX_COLS):
            if (i, j) not in user_session:
                print('X', end=' ')
            else:
                print(grid[i][j], end=' ')
        print()