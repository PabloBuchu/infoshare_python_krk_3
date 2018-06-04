ADMIN_USERNAME = 'Piotr'
name = input('Podaj imie: ')

name_capitalized = name.lower().capitalize()

if name_capitalized == ADMIN_USERNAME:
    print('Hey', name)
else:
    print('Hey Poklikash?!')

# TODO: some comment