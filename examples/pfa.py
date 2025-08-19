# Original function
def multiply(x, y):
    return x * y

# Create a PFA, using function factory
def make_multiplier(factor):
    def multiplier(num):
        return multiply(factor, num)
    
    return multiplier

by_5 = make_multiplier(5)
print(by_5(3))