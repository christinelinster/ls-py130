# Basic Generator Function

def numbers():
    for num in range(1,6):
        yield num

for num in numbers():
    print(num)