## Problem 1 ##
s = 'django'
s[0]
s[-1]
s[:4]
s[1:4]
s[-2:]
s[::-1]
## Problem 2 ##
l = [3,7,[1,4,'hello']]
l[2][2] = 'goodbye'
l
## Problem 3 ##
d1 = {'simple_key':'hello'}
d1['simple_key']
d2 = {'k1':{'k2':'hello'}}
d2['k1']['k2']
d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
d3['k1'][0]['nest_key'][1]
## Problem 4 ##
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]
set(mylist)
## Problem 5 ##
print("Hello my dog's name is {name} and he is {age} years old".format(name='sammy', age=4))


