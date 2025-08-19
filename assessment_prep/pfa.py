def create_power_func(exponent):
    def inner(base):
        return base ** exponent
    return inner 

power_of_two = create_power_func(2)
print(power_of_two(5))  # Expected output: 25
print(power_of_two(10)) # Expected output: 100

power_of_three = create_power_func(3)
print(power_of_three(2)) # Expected output: 8
print(power_of_three(3)) # Expected output: 27