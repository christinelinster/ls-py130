string = ['This', 'is', 'the', 'capitalized', 'version!']

def capitalize(string):
    for word in string:
        yield word.capitalize()

print(tuple(capitalize(string)))