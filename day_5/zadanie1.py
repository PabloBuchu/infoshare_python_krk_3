duplicates = [1, 2, 5, 1, 4, 7, 2, 6, 5, 10, 10, 30, 10, 10]

without_duplicates = []

# iterujac sie po kazdym elemencie z listy duplicates
# dodaj elementy do listy without_duplicates tylko jezeli
# juz sie w niej nie znajduje (lista ma nie zawierac duplikatow)

for element in duplicates:
    if element not in without_duplicates:
        without_duplicates.append(element)

print(without_duplicates)