#tuples are like lsits that are immutable - use for calendar dates, days of the week
#### Constructing Tuples ###
t = ('one',2)
t
t[0]
t[-1]
# Use .index to enter a value and return the index
t.index('one')
# Use .count to count the number of times a value appears
t.count('one')
# Because of this immutability, tuples can't grow.
# Once a tuple is made we can not add to it.

############## SETS AND BOOLEANS #######################
### Sets ###
# Sets are an unordered collection of *unique* elements.
x = set()
x.add(1)
x.add(2)
x
#will not add the 1 as already exists - must be unique
x.add(1)
x
#We can cast a list with multiple repeat elements to a set to get the unique elements.
lst = [1,1,2,2,3,4,5,6,1,1]
lst
set(lst)
#does not alter the original list
lst
######## Booleans ########
a = True
a
#Output is boolean value
1 > 2
# We can use None as a placeholder for an object that we don't want to reassign yet:
b = None
b
