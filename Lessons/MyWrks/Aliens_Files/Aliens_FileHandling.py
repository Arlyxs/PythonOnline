# allows reading of file in simple text format
f = open('Aliens_Files\MyData.txt', 'r')

print(f.read())
print('====')

f = open('Aliens_Files\MyData.txt', 'r')
# read is open *1 
print(f.readline())
print('====')
print(f.readlines())


'''
*1 ... so will read one line then all others when second print is called. 

value in readline(2) truncates text to 2 letters
value in readlines truncates text also
'''
