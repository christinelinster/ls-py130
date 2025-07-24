
def reciprocal(n):
    for num in range(1, n + 1):
        yield 1/num

for num in reciprocal(7):
    print(num)