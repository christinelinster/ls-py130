string = ['This', 'is', 'the', 'capitalized', 'version!']
capitalized = (word.capitalize() for word in string)

print(tuple(capitalized))