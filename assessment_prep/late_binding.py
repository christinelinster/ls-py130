def create_multipliers():
    multipliers = []
    for i in range(3):
        def multiplier(x, i=i):
            return x * i
        multipliers.append(multiplier)
    return multipliers

multipliers = create_multipliers()

print(multipliers[0](10)) # Expected: 0
print(multipliers[1](10)) # Expected: 10
print(multipliers[2](10)) # Expected: 20

'''
The code doesn't work due to late-binding. This occurs when the free variables (the non-local variable 
from the enclosing scope that the closure references) are bound when the multiplier function is called, not when its created.
The value of the free variable is the final value when the outer function, create_multipliers finished excuting, which is 2.
To fix this, we can provide the free variable as a default argument
'''