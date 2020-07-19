'''

'''

import mysql.connector


# Connection
mydb = mysql.connector.connect(host = "localhost", user = "yatish" , passwd = "1234", database = "TestDatabase")

# We need this cursor like how we have 'statement' in java, which will call 'execute'
mycursor = mydb.cursor()

#execute the statement
mycursor.execute("select * from student")

# 'mycursor' variable will have the results. if you want to assign it to another variable then you can use 'fetchall()'
result = mycursor.fetchall()

result1 = mycursor.fetchone()

# for loop is iterating over each row 
for each in result
    print(each)

