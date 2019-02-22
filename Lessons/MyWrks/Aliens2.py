# user input itn or float or str
import sys
x = int(input('enter 1st number '))
y = int(input('enter 2nd number '))
z = x + y
print(z)

# fetch first fharacter on input
ch = input('enter a characer ')
print(ch[0])

chrt = input('enter a char ')[0]
print(chr)

result = eval(input('enter an expression'))
print(result)

# index first index [0] is for file name
# navigate to file in cmd prompt and enter numbers with space between
a = int(sys.argv[1])
b = int(sys.argv[2])
c = a + b
print(c)

# for loop with if do not print 5s
for i in range(1, 21):
    if i % 5 != 0:
        print(i)

# print range bckwards
for i in range(20, 11, -1):
    print(i)

# continue in for loop - goes on after condition met
for i in range(5):
    if i == 3:
        continue
    print('hello ', i)
