####--FUNCTIONS--#####
# Formally, a function is a useful device that groups together a set of statements so they can be run more than once. They can also let us specify parameters that can serve as inputs to the functions.  functions allow us to not have to repeatedly write the same code again and again.

# def Statements ###

def hello():
    print('hello')
#call the function
hello()

def giveMeHello():
    return "hello"

result = giveMeHello()
print(result)
# or print(giveMeHello())

def evenCheck(num):
    print("I'm checking to see if {} is even!".format(num))
    # Experienced way: (Don't need an if statement)
    print(num % 2 == 0)

#call the function
evenCheck(45)

def helloYou(name="Default Name"):
    return("Hello, "+name)

# Try this with and without a name
result = helloYou()
print(result)
#call the function
helloYou('Lyxi')

# function that will add two numbers together, only if they are even!
def addEvenOnly(num1, num2):
    """
    input two nums
    output false if both nums not even
    sum if both even
    """
    if (num1 % 2 != 0) or (num2 % 2 != 0):
        return False
    else:
        return num1 + num2


x = addEvenOnly(1, 2)
y = addEvenOnly(4, 4)
print(x)
print(y)

a=int
b=int
c=int
if a > b and c > a:
  print("Both conditions are True")

if a > b or a > c:
  print("At least one of the conditions is True")



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
print(list(evens))

# Methods
st = 'hello my name is Sam'
st.lower()
st.upper()
st.split()

tweet = 'Go Sports! #Sports'
tweet.split('#')
tweet.split('#')[1]

d = {'k1':1,'k2':2}
d.keys()
d.items()

lst = [1,2,3]
x = lst.pop()

# in Operator (not a method, just something useful)
'x' in [1,2,3]
'x' in ['x','y','z']
