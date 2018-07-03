class Shape:
    def area(self):
        raise NotImplementedError()


s = Shape()
s.area()


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b



class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)


a = 10
b = 20
foo = Rectangle(a, b)
print("a: ", foo.a)
# print("b: ", foo.b)
# print("area: ", foo.area())

foo2 = Square(10)
# print(foo2.area())
# print(isinstance(foo2, Square))
print(issubclass(Shape, Square))
