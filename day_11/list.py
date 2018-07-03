def foo(a, l=None):
    if not l:
        l = []
    l.append(a)
    print(l)

foo(1)
foo(2)
foo(3)