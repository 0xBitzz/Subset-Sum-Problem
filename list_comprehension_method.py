# Subset Sum Problem to obtain a given target from the given Array elements

# Using list comprehension
from itertools import combinations


def func(args, target):
    sub_arrays = []
    for arg in range(len(args)):
        sub_arrays += list(combinations(args, arg))
    sub_arrays = [list(v) for v in sub_arrays if len(v) != 0 and sum(list(v)) == target]
    result = sub_arrays, len(sub_arrays)
    return f'{target} can be found in {args} {result[1]} times. This is/are the subarray(s) {result[0]}\n'


print(func([3, 2, 1, 7, 20], 10))
print(func([0, 0, 0], 0))
