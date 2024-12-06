
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


with open('input_sm') as input_file:
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
    visited_would_loop = set()
    visited_possible_object_placement = set()

    def step():

        next_pos = (player[0][0] + player[1][0], player[0][1] + player[1][1])

        if next_pos in obstacles:
            # player rotates
            player[2] = (player[2] + 1) % 4
            player[1] = directions[player[2]]
            return

        relative_right_dir = directions[(player[2] + 1) % 4]

        # if we come across a previous position, and were we to turn right,
        # would be going the same direction as the previous direction
        # then that would be a loop
        if (player[0], directions[relative_right_dir]) in visited_would_loop:
            visited_possible_object_placement.add(next_pos)

        visited.add(player[0])

        # log previously visited position + direction
        visited_would_loop.add((player[0], player[1]))
        player[0] = next_pos

    while is_in_bounds(player[0], grid_bounds):
        step()

    print(len(visited), len(visited_would_loop), len(visited_possible_object_placement))

    row_len = len(grid[0])
    for y in range(0, len(grid)):
        for x in range(0, row_len):
            if (x,y) in visited_possible_object_placement:
                print('O', end='')
            print(grid[y][x], end='')

        print()