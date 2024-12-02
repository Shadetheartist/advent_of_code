import math
sign = lambda x: math.copysign(1, x) # two will work

def is_safe(report):
    s = 0
    for i in range(0, len(report) - 1):
        a = report[i]
        b = report[i + 1]
        x = a - b

        if abs(x) < 1:
            return False

        if abs(x) > 3:
            return False

        ss = sign(x)
        if s != 0 and ss != 0 and s != ss:
            return False

        s = ss

    return True

with open('input') as file:
    lines = [line.rstrip().split('   ') for line in file]
    reports = list(map(lambda r: list(map(int, r[0].split(' '))), lines))
    safes = 0
    for r in reports:
        safes += 1 if is_safe(r) else 0

    print(safes)