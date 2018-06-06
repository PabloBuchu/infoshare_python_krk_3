# TODO: pobierz od uzytkownika liczbe, ktora bedzie gorna granica zakresu
# TODO: w danym zakresie zlicz liczby parzyste i nieparzyste


upper_boundary = int(input('Podaj liczbe: '))
odds = 0
evens = 0

for value in range(0, upper_boundary + 1):
    if value % 2:
        odds += 1
    else:
        evens += 1

print('Nieparzyste', odds)
print('Parzyste', evens)






















