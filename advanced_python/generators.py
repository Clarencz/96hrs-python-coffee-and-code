def mygenerator(n):
    # yield
    for x in range (n):
        yield x**3

values = mygenerator(3000)
print(next(values))
print(next(values))
