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
f = open('Aliens_Files\MyData.txt', 'r')

f3 = open('Aliens_Files\Cpy.txt', 'w')

for data in f:
    f3.write(data)

'''
file empty after first run.  data shows in second run

to copy image or other binary non-character file 
use rb (read binary) and wb (write binary) as mode
e.g.    f = open('IMG_90', 'rb')
        f = open('MyPic', 'wb)
'''
