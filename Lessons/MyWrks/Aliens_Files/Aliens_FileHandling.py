# allows reading of file in simple text format
f = open('Aliens_Files\MyData.txt', 'r')

print(f.read())
print('====')

f = open('Aliens_Files\MyData.txt', 'r')
# read is open *1
print(f.readline(), end='#')
print(f.readline())
print('====')
print(f.readlines())


'''
*1 ... so will read one line then all others when second print is called.
end='#' avoids new line

value in readline(2) truncates text to 2 letters
value in readlines truncates text also
'''

# allows saving of a file
f1 = open('Aliens_Files\Abc.txt', 'w')
f1.write('something, ')
f1.write('about people:')
f1.writelines(' makes me mad, can get me happy')

# allows appending of data to an existing file
f2 = open('Aliens_Files\Abc.txt', 'a')
f2.write(' THIS was appended')

# copy all data from one file to another
f3 = open('Aliens_Files\Cpy.txt', 'w')
f = open('Aliens_Files\MyData.txt', 'r')

f3 = open('Aliens_Files\Cpy.txt', 'w')

for data in f:
    f3.write(data)

'''
file must already exist to write data on first run.
'''
