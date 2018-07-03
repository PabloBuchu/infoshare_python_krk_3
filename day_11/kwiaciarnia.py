class Kwiat:
    def __init__(self, cena, rodzaj):
        self.cena = cena
        self.rodzaj = rodzaj

    def __str__(self):
        return self.rodzaj

    def __repr__(self):
        return self.__str__()


class Bukiet:
    def __init__(self, zbior_kwiatow):
        self.zbior_kwiatow = zbior_kwiatow

    def cena(self):
        cena = 0
        for kwiat in self.zbior_kwiatow:
            cena += kwiat.cena

        return cena


class Kwiaciarnia:
    def __init__(self):
        self.kwiaty = []
        self.bukiety = []

    def dodaj_bukiet(self, bukiet):
        self.bukiety.append(bukiet)

    def dodaj_kwiat(self, kwiat, ilosc=1):
        for i in range(ilosc):
            self.kwiaty.append(kwiat)


tulipan = Kwiat(5, 'tulipan')
print(tulipan.rodzaj)
print(tulipan.cena)

b = Bukiet([tulipan, tulipan])
print(b.zbior_kwiatow)
print("Cena: ", b.cena())

kw = Kwiaciarnia()
kw.dodaj_bukiet(b)
kw.dodaj_kwiat(tulipan, ilosc=10)

print(kw.bukiety)
print(kw.kwiaty)