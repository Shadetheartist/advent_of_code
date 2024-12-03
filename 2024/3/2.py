import re

with open('input') as file:
    input = file.read()
    t = 0
    enable = True
    for m in re.finditer("mul\((\d+),(\d+)\)|do\(\)|don't\(\)", input):
        if m.group() == 'don\'t()':
            enable = False
        if m.group() == 'do()':
            enable = True
        if enable and m.groups()[0] is not None:
            a, b = m.groups()
            a, b = int(a), int(b)
            t += a * b
    print(t)