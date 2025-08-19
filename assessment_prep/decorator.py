def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"The name of the function is: {func.__name__}")
        result = func(*args, **kwargs)
        return result
    return wrapper
# Decorator to be created
# def log_call(func):
#     ...

@log_call
def add(a, b):
    return a + b

@log_call
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

add(3, 5)
greet("World")
greet("Alice", greeting="Hi")