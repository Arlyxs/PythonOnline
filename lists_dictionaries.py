#lists are mutable, can contain different object types
my_list = [1, 2, 3]
my_list
my_list1 = ['A string', 23, 100.232, 'o']
my_list1

#indexing and slicing works just like strings
my_list1[0]
my_list1[3]
my_list[:1]
my_list1[:2]

#can concatenate lists (does not change original)
my_list1 + ['new item']
#use multiplication (not permanent)
my_list1 * 2

l = [1, 2, 3]
#permanently append to the list
l.append('append me')
l
#pop to remove item from list
l.pop(0)
l
popped_item = l.pop()
popped_item
l
#use sort and reverse list methods
new_list = ['a','e','x','b','c']
#permanently reverse the order
new_list.reverse()
new_list
new_list.sort()
new_list

# ##nested lists
lst_1 = [1, 2, 3]
lst_2 = [4, 5, 6]
lst_3 = [7, 8, 9]

matrix = [lst_1, lst_2, lst_3]
matrix

# nested indexing
matrix[0]
matrix[0][0]

# Build a list comprehension by deconstructing a for loop within a []
first_col = [row[0] for row in matrix]
first_col

#    ### Dictionaries ###
#Mappings are a collection of objects that are stored by a key, unlike a sequence that stored objects by their relative position.
# This is an important distinction, since mappings won't retain order since they have objects defined by a key.
# A Python dictionary consists of a key and then an associated value. That value can be almost any Python object.

my_dictA = {'key1': 'value1', 'key2': 'value2'}
my_dictA
# Call values by their key
my_dictA['key2']

my_dict = {'key1':123,'key2':[12,23,33],'key3':['item0','item1','item2']}

#Lets call items from the dictionary
my_dict['key3']

# Can call an index on that value
my_dict['key3'][0]

#Can then even call methods on that value
my_dict['key3'][0].upper()

# We can effect the values of a key as well. For instance:
my_dict['key1']

# Subtract 123 from the value
my_dict['key1'] = my_dict['key1'] - 123
# OR my_dict['key1'] -= 123
#Check
my_dict['key1']

#create keys be assignment
d = {}
d['animal'] = 'dog'
d['answer'] = 42
d

# Nesting Dictionaries in dictionaries ###
# Dictionary nested inside a dictionary nested in side a dictionary
d = {'key1':{'nestkey':{'subnestkey':'value'}}}

# grab that value by -  Keep calling the keys
d['key1']['nestkey']['subnestkey']

di = {'key1':1,'key2':2,'key3':3}
# Method to return a list of all keys
di.keys()
# Method to grab all values
di.values()
# Method to return tuples of all items  (we'll learn about tuples soon)
di.items()









