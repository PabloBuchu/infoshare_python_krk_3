names = ['pawel', 'michal', 'magda', 'ania', 'paulina']

print('dlugosc listy names to', len(names))

first_element = names[0]
last_element = names[-1]

# dodawanie elementu na koniec listy

names.append('sebastian')
print('aktualny stan listy po append', names)
print('ostatni element', names[-1])

name_to_find = 'przemek'
przemek_count = names.count(name_to_find)
print('liczba osob o imieniu', name_to_find, przemek_count)

name_to_find = 'ania'
names.append(name_to_find)
print('liczba osob o imieniu', name_to_find, names.count(name_to_find))

idx = names.index(name_to_find)
print('index of', name_to_find, idx)

# sprawdz czy name_to_find znajduje się w liscie names
# jesli tak to wyswietl komunikat
# `in`
if name_to_find in names:
    print('found!')
else:
    print('not found')

second_row = names[1:3]
print(second_row)

# wyswietl kazdy element listy names korzystajac z petli
# TODO: for element in kolekcja

for name in names:
    print(name)

additional_names = ['piotrek', 'kasia']

# names.extend(additional_names)
# print(names)

my_list = names + additional_names
print(my_list)

name_to_remove = 'ania'
my_list.remove(name_to_remove)
print('after removal', my_list)

# removed_item = my_list.pop(5)
# print(removed_item)
my_list.pop()
print(my_list)

del my_list[2]
del names

print(names)

something = None