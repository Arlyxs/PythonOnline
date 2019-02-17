def greeting(name):
	print("Hello, " + name)

import mymodule
mymodule.greeting("Jonathan")
#
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

import mymodule
a = mymodule.person1["age"]
print(a)
#
#You can create an alias when you import a module, by using the as keyword:
#Example
#Create an alias for mymodule called mx:

import mymodule as mx

a = mx.person1["age"]
print(a)

#Bult in Modules
import platform

x = platform.system()
print(x)

import platform

x = dir(platform)
print(x)

#You can choose to import only parts from a module, by using the from keyword.

#Example
#The module named mymodule has one function and one dictionary:

def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

#Import only the person1 dictionary from the module:

from mymodule import person1

print (person1["age"])

#RegEx Module
#Python has a built-in package called re, which can be used to work with Regular Expressions.

Import the re module:

import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
