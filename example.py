file = open('example.txt', 'r')
content = file.read()
file.close()

print(repr(content))