a = 5
b = 0

try:
    print('resource open')
    b = int(input('enter a number'))
    print(a/b)

except ZeroDivisionError as e:
    print('hey you cannot divide by 0: code error::', e)

except ValueError as e:
    print('invalid input')

except Exception as e:
    print('something went wrong...')

finally:
    print('resource closed')
