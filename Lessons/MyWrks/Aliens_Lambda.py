from functools import reduce
# filter, map, reduce
nums = [3, 2, 6, 8, 4, 6, 2, 9]
print(nums)
evens = list(filter(lambda n: n % 2 == 0, nums))
print(evens)
doubles = list(map(lambda n: n * 2, evens))
print(doubles)
sum = reduce(lambda a, b: a + b, doubles)
print(sum)

print('############\n')
# decorators add features to existing functions
# Always numerator should be bigger than the denominator


def div(a, b):
    print(a / b)


def smart_div(func):
    def inner(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)
    return inner


div = smart_div(div)

div(2, 4)
print('############\n')
