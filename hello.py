# now, to clear the screen
import os
cls = lambda: os.system('cls')
cls()

import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

msg = "Hello World"
print(msg)
wrd = "My Lord is law"
print(wrd)

#user input
my_name = input()
my_name

s='whattherass'

word_list = []
for elem in s[::]:
    word_list.append(elem)
    print(word_list)

#split numbers that user input into a list [1,2,3]
a=[]
p=input()    
for i in p:
    a.append(int(i))
print(a)

    # Lambda Expressions
#an anonymous function when full function is not required
def timesTwo(num):
    return num*2
# Lambda expression
lambda num: num*2

my_list = [1,2,3,4,5,6,7,8,9,10]
def evenBool(num):
    return num%2 == 0
evens = filter(evenBool,my_list)
print(list(evens))

# Now with Lambda!
evens = filter(lambda num: num%2==0,my_list)
print(len(list(evens)))
#print(list(evens))