def select(callback, iterable):
    selected = []
    for item in iterable:
        if callback(item):
            selected.append(item)

    return selected

# Using comprehensions
def select(callback, iterable):
    return [item for item in iterable if callback(item)]

numbers = [1, 2, 3, 4, 5]
colors = {'red', 'orange', 'yellow', 'green',
          'blue', 'indigo', 'violet'}

odd_numbers = select(lambda number: number % 2 != 0, numbers)
print(odd_numbers)            # [1, 3, 5]

large_numbers = select(lambda number: number >= 10, numbers)
print(large_numbers)          # []

small_numbers = select(lambda number: number < 10, numbers)
print(small_numbers)          # [1, 2, 3, 4, 5]

short_color_names = select(lambda color: len(color) <= 5, colors)
print(short_color_names)      # ['blue', 'red', 'green']
# The order of the colors may vary, but should include the
# indicated colors.