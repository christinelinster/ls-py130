# Generator Function
def unlimited_sequence():
    num = 1
    while True:
        yield num
        num = num * 2 + 1

sequence = unlimited_sequence()
for i in range(5):
    print(next(sequence))

# Generator Expression 
square_nums = (num**2 for num in range(1, 11))
for num in square_nums:
    print(num)