def describe_pet(animal_type, *, name=''):
    print(f'I am a {animal_type} named {name}')


print(describe_pet("Hamster", name="Harry"))
# The animal is a Hamster and its name is Harry.

describe_pet("Cat", "Dog", name="Pepe")
# TypeError: describe_pet() takes 1 positional argument but
# 2 positional arguments (and 1 keyword-only argument) were
# given