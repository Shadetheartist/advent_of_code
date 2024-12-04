
def val(x, y, matrix, size):
    if 0 <= x < size[0] and 0 <= y < size[1]:
        return matrix[y][x]
    else:
        return None


def search(x, y, matrix, size):
    center_val = val(x, y, matrix, size)

    # if this isn't one of the terminals of an XMAS (X or S) then don't traverse
    if center_val != 'A':
        return 0

    tr_o = (+1, -1)
    bl_o = (-1, +1)
    tl_o = (-1, -1)
    br_o = (+1, +1)

    tr_p = x + tr_o[0], y + tr_o[1]
    bl_p = x + bl_o[0], y + bl_o[1]
    tl_p = x + tl_o[0], y + tl_o[1]
    br_p = x + br_o[0], y + br_o[1]

    tr = val(tr_p[0], tr_p[1], matrix, size)
    bl = val(bl_p[0], bl_p[1], matrix, size)
    tl = val(tl_p[0], tl_p[1], matrix, size)
    br = val(br_p[0], br_p[1], matrix, size)

    if ((tl == 'S' and br == 'M') or (tl == 'M' and br == 'S')) and ((tr == 'S' and bl == 'M') or (tr == 'M' and bl == 'S')):
        return 1

    return 0

with open('input') as file:
    data = [line.strip().split() for line in file]
    matrix = [list(row[0]) for row in data]
    size = (len(matrix[0]), len(matrix))

    t = 0

    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            t += search(x, y, matrix, size)

    print(t)
