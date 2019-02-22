# user input
my_name = input()
my_name
# 2**3 gives 2 to the power three
# 4**.5 give quare root

# stores the value of 5 in a lable called a
a = 5
a+a

# division
x = 10 / 3  # returns double
x = 10 // 3  # returns int
x = 10 ** 3  # returns exponent (left to the power right)
# augmented assignment operator
# can use any of the std operators in front of = operator eg
x += 1
x **= 4
print(x)
# does nto have increment operators like x++ or x--

# labels in lowercase no spaces and restricted symbols
my_income = 100
tax_rate = .01
my_taxes = my_income*tax_rate
# Show my taxes
my_taxes
# strings
# strings use single or double qyuotes to let python remember the sequence of letters
# strings are stored as a sequene of characters thus can be indexed and searched
# strings are created using either single or double quotes around characters
'hello'
"hello"
# use combinations of single and double quotes to escape errors
"Now I'm ready to use single quotes in a string"
# ## Printing a String
# correct way to display strings in output is to print them
print('Hello World 1')
print('Hello World 2')
print('Use \n to print a new line')
print('\n')
print('See what I mean?')

# len checks the length of a string
# index starts at zero
len('hello world')
# assign a label to a string
#label or identifier
s = 'hello world'
s
print(s)
len(s)
# indexing strings (index starts from 0)
s[0]
s[4]
# ###slicing (use a : to grab up to a point)
# grab everything past first character
s[1:]
# grab up to but not including the 3rd index
s[:3]
# grab everything
s[:]
# ##negative indexing allows us to go backwards
# one index behind 0 so loops back around to last letter
s[-1]
# grab all but the last letter
s[:-1]
# grab in step sizes
s[::1]
s[::2]
# print a string backwards
s[::-1]
# strings are immutable and cannot be changed eg s[0]='x'
# ##concatenate strings
s + ' concatenate me'
# does not change the value of s

# ##use multiplication to create repitition
letter = 'zed'
letter*10

# ##Object methods Object.method(paramaters)
s.upper()
s.lower()
s.split()
# excludes the element it was split on
s.split('w')

# use the string .format() method to format objects into your strings
# 'string here {var1} then also {var2}'.format(var1='something', var2='somthing2)
print('This is a string with an {p}'.format(p='insert'))
print('One: {p}, Two: {p}, Three: {p}'.format(p='Hi!'))
print('Object 1: {a}, Object 2: {b}, Object 3: {c}'.format(
    a=1, b='two', c=12.3))

# use formatted strings
first = 'Aleix'
last = 'Culture'
full = f'{first} {last}'
print(full)

fulls = f'{len(first)} {2 + 2}'
print(fulls)

# evalueate if character sequence present by string value
s1 = 'welcome'
print('come' in s1)
print('come' not in s1)

s = "welcome to python"
s.endswith("thon")
# True
s.startswith("good")
# False

course = '   Python Programming'
print(course)
print(course.lower())  # to lowercase
print(course.title())  # capitalise first letter of each word
# remove leading and trailing spaces(rstrip or lstrip params)
print(course.strip())
print(course.find('pro'))  # find index of
print(course.replace('P', '_'))  # replace character
