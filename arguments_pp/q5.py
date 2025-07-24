def find_person(**kwargs):
    for name, profession in kwargs.items():
        if name == 'Antonina':
            print(f"{name}'s profession is {profession}")
            return
    print('Antonina not found')


find_person(John="Engineer", Antonina="Software Engineer")
# Antonina's profession is Software Engineer

find_person(John="Engineer", Ginni="Software Engineer")
# Antonina not found