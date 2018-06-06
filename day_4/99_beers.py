# TODO: na ekranie ma sie wyswietlac odliczanie
# TODO: od 99 do 0
# TODO: 'X beczek piwa na polce stalo, jedna spadla Y zostalo'

beers = range(99, 0, -1)

for beer in beers:
    print(f'{beer} beczek piwa na polce stalo, jedna spadla {beer - 1} zostalo')

