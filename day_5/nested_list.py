chemia = ['proszek do prania', 'mydlo', 'pasta do zebow']
warzywa = ['burak', 'marchewka', 'pietruszka', 'seler']

zakupy_czerwiec = [chemia, warzywa]
# print(zakupy_czerwiec)

zakupy_lipiec = zakupy_czerwiec.copy()
# print(zakupy_lipiec)
zakupy_lipiec[1].append('ogorek')
print(zakupy_lipiec)
print(zakupy_czerwiec)