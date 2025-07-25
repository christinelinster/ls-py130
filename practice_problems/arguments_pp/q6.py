def concat_strings(*args, sep=' '):
    return sep.join(args)

print(concat_strings("Hello", "world!"))              # Hello world!
print(concat_strings("one", "two", "three", sep='+')) # one+two+three