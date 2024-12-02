from collections import Counter
with open('input') as file:
    lines = [line.rstrip().split('   ') for line in file]
    left, right = zip(*lines)
    left, right = list(map(int, left)), list(map(int, right))
    left.sort()
    right = Counter(right)

    similarity = 0
    for n in left:
        s = n * (right.get(n) or 0)
        similarity += s
        print(n,  (right.get(n) or 0), s, similarity)

    print(similarity)