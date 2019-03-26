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

print('#########\n')
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
print('#########\n')

# factorial


def fact(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f


x = 4
result = fact(x)

print(result)
print('#########\n')
# recursion - calling a function from itself (a function from a function)
# by default maximum is 1000 recurrsions
# to change the limit:
'''
import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())
'''
# using recursion to find a factorial


def fact(n):
    if(n == 0):
        return 1

    return n * fact(n - 1)


result = fact(5)
print(result)
print('#########\n')
