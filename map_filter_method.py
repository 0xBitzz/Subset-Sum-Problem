# Subset Sum Problem to obtain a given target from the given Array elements

# Using map, lambda and filter
from itertools import combinations


def func(args, target):
    sub_arrays = []
    for arg in range(len(args)):
        sub_arrays += list(combinations(args, arg))
    sub_arrays = list(map(lambda x: list(x), filter(lambda x: len(x) != 0 and sum(x) == target, sub_arrays)))
    result = sub_arrays, len(sub_arrays)
    return f'{target} can be found in {args} {result[1]} time(s). This is/are the subarray(s) {result[0]}\n'


print(func([3, 2, 1, 7, 20], 10))
print(func([0, 0, 0], 0))
