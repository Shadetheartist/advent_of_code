import json
import math
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
            return False, i

        if abs(x) > 3:
            return False, i

        ss = sign(x)
        if s != 0 and ss != 0 and s != ss:
            return False, i

        s = ss

    return True, -1


def without(arr, idx):
    if idx < 0:
        return arr
    return [x for i, x in enumerate(arr) if i != idx]

solutions = dict()
with open('solutions') as file:
    solutions = json.load(file)


print(solutions)

with open('input') as file:
    lines = [line.rstrip().split('   ') for line in file]
    reports = list(map(lambda r: list(map(int, r[0].split(' '))), lines))
    safes = 0
    for n,r in enumerate(reports):

        safe, issue_idx = is_safe(r)

        if safe:
            safes += 1
        else:
            safe_0 = False

            if (issue_idx < 2 and is_safe(without(r, 0))[0]) or is_safe(without(r, issue_idx))[0] or is_safe(without(r, issue_idx+1))[0]:
                safes += 1
            elif str(n) in solutions:
                print(
                    r,
                    is_safe(r),
                    without(r, issue_idx),
                    is_safe(without(r, issue_idx)),
                    n,
                    solutions[str(n)] if str(n) in solutions else 'None'
                )
    print(safes)

print(is_safe_calls)