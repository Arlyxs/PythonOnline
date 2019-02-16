## COMPARISON OPERATORS ###
1 > 2
1 < 2
1 >= 1
1 <= 4
1 == 1
1 == '1'
'hi' == 'bye'
1 != 2
(1 > 2) and (2 > 3)
(1 > 2) or (2 < 3)
(1 == 2) or (2 == 3) or (4 == 4)

#Indentation is extremely important in Python and is basically Python's way of getting rid of enclosing brackets like {} Code blocks are then noted by a colon (:)
### if,elif, else Statements #####
if 1 < 2:
    print('Yep')

if 1 < 2:
    print('first')
else:
    print('last')

if 1 == 2:
    print('first')
elif 3 == 3:
    print('middle')
else:
    print('Last')

### FOR LOOPS #######
## For Loop with a list

# Perform an action with each element without actual list element
seq = [1,2,3,4,5]
for elem in seq:
    print(elem)
for item in seq:
    print('yep')

## For Loop with a Dictionary ##
ages = {"Sam":3,"Frank":4,"Dan":29}
for elem in ages:
    print("This is the key")
    print(elem)
    print("This is the value")
    print(ages[elem])
    print("\n")

##tuple pair data return ##        
mypairs = [(1,10),(3,30),(5,50)]
# Normal
for tup in mypairs:
    print(tup)
# Tuple un-packing
for elem1,elem2 in mypairs:
    print(elem1)
    print(elem2)

### WHILE LOOPS #######
# While loops allow us to continually perform and action until a condition becomes true. For example:
i = 1
while i < 5:
    print('i is: {}'.format(i))
    i = i+1
# i = i+1 is used to break the loop to ensure that it does not run forever

# RANGE FUNCTION
# range() can quickly generate integers for you, based on a starting and ending point
range(5)

list(range(5))

for elem in range(5):
    print(elem)

list(range(1,11))

list(range(0,10,2))

x = [1,2,3,4]
# Written in List Comprehension Form
out = [item**2 for item in x]
print(out)


