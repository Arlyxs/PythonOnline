# yield is a generator the returns iteration values
def topten():
    yield 1
    yield 2
    yield 3
    yield 4


values = topten()

print(values.__next__())
print(values.__next__())

for i in values:
    print(i)

print('=========')


# yield does not terminate the function as return does
def TopTens():
    n = 1

    while n <= 10:
        sq = n*n
        yield sq
        n += 1


valuess = TopTens()

for i in valuess:
    print(i)
