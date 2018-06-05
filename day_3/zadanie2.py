# TODO: napisz program ktory sprawdzi czy liczba jest parzysta
# TODO: liczba do sprawdzenia jest podawana przez uzyszkodnika

value = input('Podaj liczbe: ')

# TODO: sprawdz czy podane dane to liczba
if value.isdigit():
    value = int(value)
    if value % 2:
        print('Nieparzysta')
    else:
        print('Parzysta')
else:
    print('Musisz podac liczbe')