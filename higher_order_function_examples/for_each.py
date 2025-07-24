def for_each(callback, iterable):
    for item in iterable:
        callback(item)

for_each(lambda number: print(number**2), [1, 2, 3, 4, 5])

pets = ('cat', 'dog', 'fish', 'bearded dragon')
for_each(lambda string: print(string.title()), pets)

nested_lists = [[1, 2], [3, 4], [5, 6, 7]]
for_each(lambda sublist: sublist.pop(), nested_lists)
print(nested_lists)