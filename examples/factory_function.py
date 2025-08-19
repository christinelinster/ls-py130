def add(x, y):
    return x + y

def make_adder(x):
    def adder(y):
        return add(x, y)
    return adder

add_five = make_adder(5)
print(add_five(10)) # 15
print(add_five.__closure__)

from functools import partial

def post(title, content):
    print(f"{title}")
    print(f"{content}")

def post_generator(title):
    def make_post(content):
        return post(title, content)
    return make_post

dev_content = post_generator("Dev Series")
dev_content("This is the first post of the series")