def increment(number, by):
    return (number, number + by)  # returns a tupple


print(increment(2, 3))


def increments(number, by):
    return (number, number + by)  # returns a tupple


# keyword argument
print(increments(2, by=3))

# assign value to parameter


def incremental(number, by=5):
    return (number, number + by)  # returns a tupple


# keyword argument
print(incremental(2))

"""This is function annotations. It can be use to attach additional information
to the arguments or a return values of functions.
It is a useful way to say how a function must be used. """


def incredible(number: int, by: int = 8) -> tuple:
    return (number, number + by)  # returns a tupple


# keyword argument
print(incredible(2))

# when you add an asterix * before a parameter python will see it
# as a tuple which is iterable eg


def multiply(*list):
    total = 1
    for elem in list:
        total *= elem
    return total


print(multiply(2, 3, 4, 5))

# creates a dictionary in the output


def save_user(**user):
    print(user)


save_user(id=1, name='admin')

# access the dictionary


def save_user(**user):
    print(user["name"], user["id"])  # or id


save_user(id=1, name='admin')

# when a variable is defined with a function it is available
# anywhere within the function not just to the indented
# "block in which it was defined"

# a global function is available anywhere in the file
# do not modify a global variable inside a function by using the keyword global
# eg
messages = 'a'


def greet():
    global messages
    messages = 'b'


greet()
print(messages)

# do not the above as it can change the value of the variable
# in other functions
# it permanantly changes messages to b for all other functions


def multiply(*numbers):
    total = 10
    for elem in numbers:
        total *= elem
    return total


print('start')
print(multiply(1, 2, 3))
print('finish')

# programming question in interviews


def fizz_buzz(input):
    if input % 3 == 0:
        return 'fizz'
    else:
        return 'buzz'


print(fizz_buzz(3))

# else statement not needed


def fizzz_buzz(input):
    if input % 3 == 0 and input % 5 == 0:
        return 'fizz_buzz'
    if input % 3 == 0:
        return 'fizzz'
    if input % 5 == 0:
        return 'buzzz'
    return input


print(fizzz_buzz(15))

# return multiple results from a function


def add_sub(x, y):
    c = x + y
    d = x - y
    return c, d


result1, result2 = add_sub(5, 4)
print(result1, result2)

# keyword to specify arguments
# also can set default value which is overidden


def person(name, age=18):
    print(name)
    print(age)


person(age=28, name='Lyxi')

# set formal variable length argument so that multiple values can be passed


def sum(*b):
    c = 0
    for i in b:
        c = c + i

    print(c)


sum(5, 6, 34, 78)

# set formal variable length argument with keyword actual argument


def person(name, **data):
    print(name)
    print(data)

    # print individual parts of the data
    for i, j in data.items():
        print(i, j)


person('Lyxi', age=28, city='POS', mobile=776 - 2222)

''' access a global variable "a" within a function use:
global a
specifically reference the variable use:
x = globals()['a']
to change the value of the global variable use:
globals()['a'] = 15
'''
# find even and odd from list


def count(lst):
    even = 0
    odd = 0

    for i in lst:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


lst = [20, 25, 14, 19, 16, 24, 28, 47, 26]

even, odd = count(lst)

print(even)
print(odd)

print('even: {} and odd: {}'.format(even, odd))

# print a fibonacci sequence


def fib(n):
    a = 0
    b = 1

    if n == 1:
        print(a)
    else:
        print(a)
        print(b)

        for i in range(2, n):
            c = a + b
            a = b
            b = c
            print(c)


fib(5)
