from itertools import product

operators = {
    '*': lambda a, b: a * b,
    '+': lambda a, b: a + b,
    '||': lambda a, b: int(str(a) + str(b)),
}

with open('input') as input_file:
    lines = [line.rstrip() for line in input_file]

    total = 0

    for line in lines:
        test_value_str, numbers_str = line.split(':')
        numbers = numbers_str.strip().split(' ')
        numbers = list(map(int, numbers))
        test_value = int(test_value_str)

        def gogopower():
            t = 0
            #print(numbers)
            for operator_combination in product(operators.keys(), repeat=len(numbers) - 1):
                #print(operator_combination)
                i = 1
                a, b = numbers[:2]
                for operator in operator_combination:
                    t = operators[operator](a, b)

                    #print(a, operator, b, '=', t)
                    if t == test_value and i == len(numbers)-1:
                        print(a, operator, b, '=', t)
                        return t

                    a = t
                    if i == len(numbers)-1:
                        break
                    i = i + 1
                    b = numbers[i]

            return 0


        total = total + gogopower()

print()
print(total)