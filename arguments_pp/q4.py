
def calculate_average(*args):
    if not args:
        return None
    return sum(args)/len(args)

print(calculate_average(1, 2, 3, 4))      # 2.5
print(calculate_average(1, 2, 3, 4, 5))   # 3.0
print(calculate_average())                # None