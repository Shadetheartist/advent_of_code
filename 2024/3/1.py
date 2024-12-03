import re

with open('input') as file:
    input = file.read()
    t = 0
    for m in re.finditer("mul\((\d+),(\d+)\)", input):
        a, b = m.groups()
        a, b = int(a), int(b)
        t += a * b

    print(t)