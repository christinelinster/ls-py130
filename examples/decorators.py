def debug_log(func):
    def wrapper(*args, **kwargs):
        print(f"The function called: {func.__name__}")
        print(f"Positional arguments: {args}")
        print(f"Keyword arguemnts: {kwargs}")

        result = func(*args, **kwargs)

        print(f"Return value: {result}")
        return result 
    return wrapper

@debug_log
def add_and_greet(a, b, greeting="Hello"):
    total = a + b
    return f"{greeting}! The sum is {total}."

add_and_greet(5, 10, greeting="Hi there")