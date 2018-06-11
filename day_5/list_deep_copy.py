import copy

chemia = ['proszek do prania', 'mydlo', 'pasta do zebow']
warzywa = ['burak', 'marchewka', 'pietruszka', 'seler']

zakupy_czerwiec = [chemia, warzywa]
# print(zakupy_czerwiec)

zakupy_lipiec = copy.deepcopy(zakupy_czerwiec)
# print(zakupy_lipiec)
zakupy_lipiec[1].append('ogorek')
warzywa_lipiec = zakupy_lipiec[1]


for kategoria_zakupow in zakupy_lipiec:
    for towar in kategoria_zakupow:
        print(towar)
    print()