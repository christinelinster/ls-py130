string = ['This', 'is', 'the', 'capitalized', 'version!']
greater_than_5 = (word.capitalize() for word in string if len(word) >= 5)
print(set(greater_than_5))

