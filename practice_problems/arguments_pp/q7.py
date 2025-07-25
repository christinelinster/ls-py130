def register(username, /, age, *, password):
    return {'username': username, 'password': password, 'age': age}

print(register('user1', 30, password='pass123'))
# {'username': 'user1', 'password': 'pass123', 'age': 30}

print(register('user2', age=45, password='pass132'))
# {'username': 'user2', 'password': 'pass132', 'age': 45}