ADMIN_USERNAME = 'Piotr'
name = input('Podaj imie: ')

# TO JEST ZMIANA DLA GITA

name_capitalized = name.lower().capitalize()

if name_capitalized == ADMIN_USERNAME:
    print('Hey', name)
else:
    print('Hey Poklikash?!')

# TODO: some comment
