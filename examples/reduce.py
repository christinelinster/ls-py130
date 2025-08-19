def reduce(callback, iterable, start):
    acc = start
    for item in iterable:
        acc = callback(item, acc)
    return acc

numbers = [10, 3, 5]
product = lambda number, accum: accum * number

# reduce(product, numbers, 2) works like this:
# 1. callback(10, 2) -> returns 20. accum is now 20.
# 2. callback(3, 20) -> returns 60. accum is now 60.
# 3. callback(5, 60) -> returns 300. accum is now 300.
# The final result is 300.

print(reduce(product, numbers, 2))     # 300