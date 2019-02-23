from math import sqrt, pow
import math as m
import math

# escape a characer in a string
print('Aleix\'s "laptop"')
# pritn a string multiple times
10 * 'Aleix'

'Aleix' * 10
# \n creates a new line when printed
print('c:\\docs\neix')

# print raw string using r gives same as escaping with \\
print('c:\\docs\\neix')
print(r'c:\docs\neix')

# to use the value from a previous output use underscore "_"
x = 10
y = 5
x + 3
_ + y

# changing lists
nums = [25, 12, 36, 95, 14, 45]
# insert 77 at index position 2
nums.insert(2, 77)
nums
# remove a specific item from the list
nums.remove(14)
nums

# remove item at index position
nums.pop(1)

# remove multiple items from a lists by index value
del nums[2:]
nums
# add multiple values
nums.extend([29, 12, 14, 36])
nums

# min max sum sort in lists
min(nums)
max(nums)
sum(nums)
nums.sort()
nums

# tuple is immutable
# sets does not support indexing, duplicate values or sequence maintenance
# convert a number from decimal to binary, octal, hexadecimal
bin(25)
oct(25)
hex(10)
0b11001
# swap values
a = 5
b = 6
# long way
temp = a
a = b
b = temp
# formula way
a = a + b
b = a - b
a = a - b
# or
a = a ^ b
b = a ^ b
a = a ^ b
# shortest way unique to python uses rotation two
a, b = b, a

print(a)
print(b)

# use imported math funcitons
x = math.sqrt(25)
print(x)
print(math.floor(2.9))
print(math.ceil(2.1))
print(math.pow(3, 2))
print(math.pi)
print(math.e)
m.sqrt(90)
pow(2, 6)
