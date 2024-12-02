with open('input') as file:
    lines = [line.rstrip().split('   ') for line in file]
    left, right = zip(*lines)
    left, right = list(map(int, left)), list(map(int, right))
    left.sort()
    right.sort()

    t = 0
    for l, r in zip(left, right):
        t += abs(l - r)
        print(l, r, abs(l - r), t)

    print(t)
