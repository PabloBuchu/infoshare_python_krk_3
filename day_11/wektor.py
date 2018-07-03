# -*- coding: utf-8 -*-
class Wektor(object):
    """Dwuwymiarowy wektor."""

    _ile_nas = 0

    def __init__(self, a, b):
        super().__init__()  # __init__(a,bclclcccasdsad)
        self.a = a
        self.b = b
        Wektor._ile_nas += 1

    def dlugosc(self):
        """Zwraca liczbę, długość Wektora."""
        return (self.a ** 2 + self.b ** 2) ** 0.5

    def obroc(self):
        """Odwraca wektor w miejscu, czyli zamienia
           wartości jego współrzędnych na przeciwne.
        """
        self.a *= -1
        self.b *= -1

    def obrocony(self):
        """Zwraca nowy wektor odwrócony."""
        return Wektor(-self.a, -self.b)

    def __str__(self):
        """Zwraca reprezentację Wektora w formie (x, y)"""
        return "(" + str(self.a) + ", " + str(self.b) + ")"

    def __repr__(self):
        """Zwraca reprezentacje Wektora w formie <Wektor(x, y) @id>"""
        return "<Wektor{0} @{1}>".format(self.__str__(), id(self))

    def __add__(self, other):
        """Zwraca nowy Wektor będący sumą self i other."""
        print("dodawanie", self, other)
        return Wektor(self.a + other.a,
                      self.b + other.b)

    def dodawanie(self, other):
        """Zwraca nowy Wektor będący sumą self i other."""
        print("dodawanie'", self, other)
        return Wektor(self.a + other.a,
                      self.b + other.b)

    def __mul__(self, other):
        """Zwraca liczbę będącą iloczynem skalarnym self i other."""
        print("mnozenie", self, other)
        return self.a * other.a + self.b * other.b

    def __del__(self):
        Wektor._ile_nas -= 1
