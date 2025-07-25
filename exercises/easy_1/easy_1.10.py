# Generator with User Input

def user_input():
    while True:
        message = input("Enter a string: ")
        if message == "stop":
            break
        yield message

    
for message in user_input():
    print(message)