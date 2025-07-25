# Remove None Values

values = [None, 1, 5, None, 0, 8, '', False]
not_none = list(filter(lambda n: n is not None, values))
print(not_none)