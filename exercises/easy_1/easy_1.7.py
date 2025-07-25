# Nested Generator Expressions

nested_list = [[1, 2, 3], [4, 5, 6], [7,8,9]]

flat_list = list((n for sublist in nested_list for n in sublist))
print(flat_list)