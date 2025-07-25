# Concatenate Strings
from functools import reduce
strings = ['this', 'is', 'the', 'first', 'message', 'in', 'this', 'program']

single_string = reduce(lambda a, b: a+b, strings)
print(single_string)