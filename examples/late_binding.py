# Late binding example
adders = []
for n in range(1, 4):
    adders.append(lambda x: x + n)

add1, add2, add3 = adders

print(f"add1(10) = {add1(10)}") # Expected: 11
print(f"add2(10) = {add2(10)}") # Expected: 12
print(f"add3(10) = {add3(10)}") # Expected: 13


# Force early binding with Default Argument to capture n's value
adders = []
for n in range(1, 4):
    adders.append(lambda x, n=n: x + n)

add1, add2, add3 = adders

# Force early binding with a Factory Function (new scope)
def adder_factory(n):
    return lambda x: x+n

adders = []
for n in range(1, 4):
    adders.append(adder_factory(n))
