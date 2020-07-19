'''

Panda's support functions to connect to DB and fetch data and store back.

'''

import pandas as pd
import sqlalchemy as sql

# This is like creating the driver to connect to the DB.
engine = sql.create_engine('mysql+pymysql://root@localhost:3306/myDB')

# This will fetch the table contents of 'Employee' table and return as a dataFrame
dataFrameFullEmployeeTable = pd.read_sql_table('Employee', engine)
# This is same as above, but we can specify required 'columns' only
dataFrameEmployeeTableOnlyNameAgeColumn = pd.read_sql_table('Employee', engine, columns=['name','age'])



'''
 I want to execute a SQL query, how do i do that?
     
'''
