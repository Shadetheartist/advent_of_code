
# indexed clockwise (turn right every 90d) = idx++
directions = (
    (+0, -1), # up
    (+1, +0), # right
    (+0, +1), # down
    (-1, +0), # left
)


def find_player_pos(grid):
    row_len = len(grid[0])
    for y in range(0, len(grid)):
        for x in range(0, row_len):
            if grid[y][x] == '^':
                return x, y
    return None


def all_obstacles(grid):
    row_len = len(grid[0])
    for y in range(0, len(grid)):
        for x in range(0, row_len):
            if grid[y][x] == '#':
                yield x, y


def grid_bounds(grid):
    return len(grid[0]), len(grid)


def is_in_bounds(pos, bounds):
    return 0 <= pos[0] < bounds[0] and 0 <= pos[1] < bounds[1]


with open('input') as input_file:
    lines = [line.rstrip() for line in input_file]
    grid = []

    for line in lines:
        row = []
        for char in line:
            row.append(char)
        grid.append(row)

    grid_bounds = grid_bounds(grid)
    print(grid_bounds)

    # start at found player pos with direction of up
    # player is tuple(pos, dir, dir_idx)
    player = [find_player_pos(grid), directions[0], 0]

    # find all the obstacles ahead of time so we can put them in a set, then we can detect them easily
    obstacles = set(all_obstacles(grid))
    visited = set()

    def step():
        next_pos = (player[0][0] + player[1][0], player[0][1] + player[1][1])
        if next_pos in obstacles:
            # player rotates
            player[2] = (player[2] + 1) % 4
            player[1] = directions[player[2]]
            print('turn')
            return

        visited.add(player[0])
        player[0] = next_pos

        print('step', player)

    while is_in_bounds(player[0], grid_bounds):
        step()

    print(len(visited))
