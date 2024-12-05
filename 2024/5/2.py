with open('input') as input_file:
    lines = [line.rstrip() for line in input_file]

    separator = lines.index("")
    rules_lines = lines[:separator]
    updates_lines = lines[separator+1:]

    rules = [tuple(map(int, rule.split('|'))) for rule in rules_lines]
    updates = [list(map(int, update.split(','))) for update in updates_lines]

    rules.sort(key=lambda x: x[1], reverse=True)

    # rule = (A, B)
    # A must be before B
    after_map = dict()
    for rule in rules:
        if rule[0] in after_map:
            after_map[rule[0]].add(rule[1])
        else:
            after_map[rule[0]] = set()
            after_map[rule[0]].add(rule[1])

    def valid_update(update):
        for i,page in enumerate(update):
            if page in after_map:
                prev_pages = update[:i]
                #print(i, page, after_map[page], prev_pages)
                for p in prev_pages:
                    # if p (from before this page) is in the 'after' map
                    # that would mean the order is wrong
                    if p in after_map[page]:
                        #print(p, 'found in after map', after_map[page], 'for page', page, 'when looking at previous pages', prev_pages)
                        return False
        return True

    valid_updates = []
    invalid_updates = []
    for update in updates:
        if valid_update(update):
            valid_updates.append(update)
        else:
            invalid_updates.append(update)

    def compare_pages(a, b):

        if a in after_map and b in after_map and b in after_map[a] and a in after_map[b]:
            print('loop', a, b)
            return 0

        # A is in the map and
        # B is in A's set
        # A must be before B
        if a in after_map and b in after_map[a]:
            #print('b in a (-1) |', b, a)
            return -1

        # B is in the map and
        # A is in B's set
        # B must be before A
        if b in after_map and a in after_map[b]:
            #print('a in b (1) |', b, a)
            return 1

        #print(a, b, '0')
        return 0

    def sort_update(update):
        i = len(update) - 1
        while i >= 0:
            j = i - 1
            while j >= 0:
                cmp = compare_pages(update[i], update[j])
                if cmp == -1:
                    tmp = update[i]
                    del update[i]
                    update.insert(j, tmp)
                    i += 1
                    break
                j -= 1
            i -= 1


    for update in invalid_updates:
        sort_update(update)

    t = 0
    for update in invalid_updates:
        center = update[len(update)//2]
        t += center

    print(t)