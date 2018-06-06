# TODO: pobierz od uzytkownika dwie liczby
# TODO: w petli while sprawdz czy a > b

# todo: wyswietl na ekranie aktualna wartosc liczby a
# TODO: jesli tak to a zmniejsz o 1

a = int(input('Podaj a: '))
b = int(input('Podaj b: '))

while a > b:
    print('Aktualna wartosc a: ', a)
    a -= 1      # a = a - 1