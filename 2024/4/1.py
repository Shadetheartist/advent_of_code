import re

next_map = {
    'X': 'M',
    'M': 'A',
    'A': 'S',
    'S': None
}

terminals = ('X', )

pos_matrix = [
    (-1, -1),
    (+0, -1),
    (+1, -1),
    (-1, +0),
    #(+0, +0),
    (+1, +0),
    (-1, +1),
    (+0, +1),
    (+1, +1),
]


def neighbourhood(x, y, matrix_size):
    global pos_matrix
    for m in pos_matrix:
        _x, _y = x + m[0], y + m[1]
        if 0 <= _x < matrix_size[0] and 0 <= _y < matrix_size[1]:
            yield (_x, _y), m


def neighbours(x, y, matrix):
    size = (len(matrix[0]), len(matrix))
    for pos, offset in neighbourhood(x, y, size):
        yield val(*pos, matrix), pos, offset


def val(x, y, matrix, size):
    if 0 <= x < size[0] and 0 <= y < size[1]:
        return matrix[y][x]
    else:
        return None


def search(x, y, matrix, size):
    center_val = val(x, y, matrix, size)

    # if this isn't one of the terminals of an XMAS (X or S) then don't traverse
    if center_val not in terminals:
        return set()

    words = set()

    for direction in pos_matrix:
        current = center_val
        elems = [(x, y)]
        for i in range(1, 4):
            nx, ny = x + direction[0] * i, y + direction[1] * i
            neighbour_val = val(nx, ny, matrix, size)
            if neighbour_val == next_map[current]:
                elems.append((nx, ny))

                # we reached an XMAS, since we only start at X,
                # we must end at S after 3 steps only if we complete the word
                if i == 3 and neighbour_val == 'S':
                    words.add(tuple(elems))
                    break
                current = neighbour_val
            else:
                # this can't be an XMAS, the next character is wrong
                break

    return words

with open('input') as file:
    data = [line.strip().split() for line in file]
    matrix = [list(row[0]) for row in data]
    size = (len(matrix[0]), len(matrix))

    words = set()
    findings = set()
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            words = words | search(x, y, matrix, size)

    print(words)
    print(len(words))
