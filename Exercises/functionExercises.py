# Complete the tasks below by writing functions! Keep in mind, these can be
# really tough, its all about breaking the problem down into smaller, logical
# steps. If you get stuck, don't feel bad about having to peek to the solutions!

#####################
## -- PROBLEM 1 -- ##
#####################

# Given a list of integers, return True if the sequence of numbers 1, 2, 3
# appears in the list somewhere.


def arrayCheck(nums):
  lst = [1, 2, 3]
  ltst = str(lst).strip("[]")
  numss = str(nums).strip("[]")
  print(ltst in numss)


arrayCheck([1, 3, 5, 7, 8, 9, 11, 14])
arrayCheck([1, 1, 2, 4, 1])
arrayCheck([1, 1, 2, 1, 2, 3])
arrayCheck([1, 2, 3])

#####################
## -- PROBLEM 2 -- ##
#####################

# Given a string, return a new string made of every other character starting  with the first,so "Hello" yields "Hlo".


def stringBits(str):
  sbits = str[::2]
  print(sbits)


stringBits('Hello')
stringBits('Hi')
stringBits('Heeololeo')

#####################
## -- PROBLEM 3 -- ##
#####################

# Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive").


def end_other(a, b):
  if a.lower().endswith(b.lower()) or b.lower().endswith(a.lower()):
    # a.lower() in b.lower() or b.lower() in a.lower():
    result = True
    print(result)
  else:
    result = False
    print(result)


end_other('Hiabc', 'abc')
end_other('AbC', 'HiaBc')
end_other('abc', 'abXabc')

#####################
## -- PROBLEM 4 -- ##
#####################

# Given a string, return a string where for every char in the original,
# there are two chars.


def doubleChar(str):
  word_list = []
  for elem in str[::]:
    word_list.append(elem)
    print(elem*2, end='')
  #print(word_list*2)


doubleChar('The')
doubleChar('AAbb')
doubleChar('Hi-There')

#####################
## -- PROBLEM 5 -- ##
#####################

# Read this problem statement carefully!

# Given 3 int values, a b c, return their sum. However, if any of the values is a
# teen -- in the range 13-19 inclusive -- then that value counts as 0, except 15
# and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that
# takes in an int value and returns that value fixed for the teen rule.
#
# In this way, you avoid repeating the teen code 3 times (i.e. "decomposition").
# Define the helper below and at the same indent level as the main no_teen_sum().
# Again, you will have two functions for this problem!

def no_teen_sum(a, b, c):
  sum = fix_teen(a) + fix_teen(b) + fix_teen(c)
  print('The adjusted sum is {val} '.format(val=sum))


def fix_teen(n):
  if n == 15 or n == 16:
    n = n
    #print(n)
  elif n >= 13 and n <= 19:
    n = 0
    #print(n)
  else:
    n = n
    #print(n)
#fix_teen(18)
  return n

no_teen_sum(1, 2, 3)
no_teen_sum(2, 13, 1)
no_teen_sum(2, 1, 14)

#####################
## -- PROBLEM 6 -- ##
#####################

# Return the number of even integers in the given array.

def count_evens(nums):
  evens = []
  for elem in nums:
    if elem % 2 == 0:
      evens.append(elem)
  print('The number of even integers is {val} '.format(val = len(evens)))

count_evens([2, 1, 2, 3, 4])
count_evens([2, 2, 0])
count_evens([1, 3, 5])

""" evens = filter(lambada elem: elem%2==0,nums)
print('The number of even integers is {val} '.format(val = len(evens))) """