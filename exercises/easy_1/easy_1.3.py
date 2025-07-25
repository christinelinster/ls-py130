# Product of Numbers
from functools import reduce

numbers = [1, 2, 3, 4, 5]
product_of_numbers = reduce(lambda a, b: a*b, numbers)
print(product_of_numbers)