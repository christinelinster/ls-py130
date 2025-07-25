def capitalized(string):
    for word in string:
        if len(word) < 5:
            yield word.capitalize()

string = ['This', 'is', 'the', 'capitalized', 'version!']
print(set(capitalized(string)))

