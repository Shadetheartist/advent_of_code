import math
import json

sign = lambda x: math.copysign(1, x)

is_safe_calls = 0
def is_safe(report):
    global is_safe_calls
    is_safe_calls += 1

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


def without(arr, idx):
    if idx < 0:
        return arr
    return [x for i, x in enumerate(arr) if i != idx]


with open('input') as file:
    lines = [line.rstrip().split('   ') for line in file]
    reports = list(map(lambda r: list(map(int, r[0].split(' '))), lines))
    safes = {}
    for n, r in enumerate(reports):
        for i in range(-1, len(r)):
            safe = is_safe(without(r, i))
            if safe:
                safes[n] = i
                break

    print(safes)
    print('n = ', len(safes))

    with open('solutions', 'w') as out_file:
        json.dump(safes, out_file)

print(is_safe_calls)