def reduce(callback, iterable, starter):
    acc = starter
    for item in iterable:
        acc = callback(item, acc)

    return acc

nums = [1, 2, 3, 4, 5, 6]

sum_squares = reduce(lambda a, b: a**2 + b, nums, 0)
print(sum_squares)
