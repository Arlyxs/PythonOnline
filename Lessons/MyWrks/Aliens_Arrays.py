# arrays must have all values of the same type
# must import the array module
# import array (array.array)
# import array as arr (arr.array)
from array import *
# i = 0
vals = array('i', [5, 9, -8, 5, 4, 2])
vals.reverse()
print(vals)
print(vals[0])

for i in range(5):
    print(vals[i])

for i in range(len(vals)):
    print(vals[i])

for e in vals:
    print(e)

# use character array
vchars = array('u', ['a', 'b', 'g'])
for x in vchars:
    print(x)

# copy from another array
newArr = array(vals.typecode, (a for a in vals))
for h in newArr:
    print(h)

# get new array with squared values of old array
newArr2 = array(vals.typecode, (a * a for a in vals))
for k in newArr2:
    print(k)

# create an array from user input and search for index position of a value


# create an array from user input
arr = array('i', [])
n = int(input('enter the length of the array '))
for i in range(n):
    x = int(input('enter the next value'))
    arr.append(x)

print(arr)

val = int(input('enter the value for search'))

k = 0
for elem in arr:
    if elem == val:
        print(k)
        break

    k += 1

print(arr.index(val))
