with open('input') as input_file:
    lines = [line.rstrip() for line in input_file]

    separator = lines.index("")
    rules_lines = lines[:separator]
    updates_lines = lines[separator+1:]

    rules = [tuple(map(int, rule.split('|'))) for rule in rules_lines]
    updates = [tuple(map(int, update.split(','))) for update in updates_lines]

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

    t = 0
    for update in valid_updates:
        center = update[len(update)//2]
        print(update, center)
        t += center

    print(t)