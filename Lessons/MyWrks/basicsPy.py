name = 'Al'
if not name:
    print('name is empty')

age = 22
if 18 <= age < 65:
    print('eligible')
  
#terniary in python
ages = 22
if age >= 18:
    message = 'eligible'
else:
    message = 'ineligible'
print(message)
#terniary verion
message = 'eligible' if ages >= 18 else 'not eligible'
print(message)

#loops
for x in 'Python':
    print(x)
for x in ['a', 'b', 'c']:
    print(x)
for x in range(5):
    print(x)

names = ['john', 'mary']
for elem in names:
    if elem.startswith('j'):
        print('found')
        break

#for else loops
namess = ['Aj', 'mary']
for elem in namess:
    if elem.startswith('j'):
        print('found')
        break
else: #note indentaion
    print('not found')

#can have a while loop with the break and else statements
guess = 0
answer = 5
while answer != guess:
    guess = int(input('guess: '))
else:
    print('you guessed correctly')
