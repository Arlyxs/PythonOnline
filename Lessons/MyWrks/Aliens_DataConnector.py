import mysql.connector

mybd = mysql.connector.connect(host='localhost',
                               user='lyxi',
                               passwd='1234',
                               database='ty3tech')

mycursor = mydb.cursor()

mycursor.execute('select * from student')

result = mycursor.fetchall() # fetchone()

for i in result:
    print(i)
