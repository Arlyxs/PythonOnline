def increment(number, by):
    return (number, number + by) #returns a tupple


print(increment(2,3))

def increments(number, by):
    return (number, number + by) #returns a tupple

#keyword argument
print(increments(2,by=3))

#assign value to parameter
def incremental(number, by=5):
    return (number, number + by) #returns a tupple

#keyword argument
print(incremental(2))

"""This is function annotations. It can be use to attach additional information
to the arguments or a return values of functions.
It is a useful way to say how a function must be used. """
def incredible(number: int, by: int=8) -> tuple:
    return (number, number + by) #returns a tupple

#keyword argument
print(incredible(2))

#when you add an asterix * before a parameter python will see it
#as a tuple which is iterable eg
def multiply(*list):
    total = 1
    for elem in list:
        total *= elem
    return total


print(multiply(2, 3, 4, 5))

#creates a dictionary in the output
def save_user(**user):
    print(user)


save_user(id=1, name='admin')

#access the dictionary
def save_user(**user):
    print (user["name"], user["id"]) #or id


save_user(id=1, name='admin')

#when a variable is defined with a function it is available
#anywhere within the function not just to the indented
#"block in which it was defined"

# a global function is available anywhere in the file
# do not modify a global variable inside a function by using the keyword global
#eg
messages = 'a'
def greet():
    global messages
    messages = 'b'

greet()
print(messages)

#do not the above as it can change the value of the variable in other functions
#it permanantly changes messages to b for all other functions

def multiply(*numbers):
    total = 10
    for elem in numbers:
        total *= elem
    return total


print('start')
print(multiply(1,2,3))
print('finish')

#programming question in interviews
def fizz_buzz(input):
    if input % 3 == 0:
        return 'fizz'
    else:
        return 'buzz'


print(fizz_buzz(3))

#else statement not needed
def fizzz_buzz(input):
    if input % 3 == 0 and input % 5 == 0:
        return 'fizz_buzz'
    if input % 3 == 0:
        return 'fizzz'
    if input % 5 == 0:
        return 'buzzz'
    return input


print(fizzz_buzz(15))
