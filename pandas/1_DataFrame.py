

# Import panda library
import pandas as pd

'''
    What is a DataFrame?
        DataFrame is a type of data.
        
    What is the data type of columns?
        'Series' is the data type of columns. its not list or tuple, make sure. 'Series' is a data type in pandas 
        library 'pandas.core.series.Series'
        
'''

'''
    We can create DataFrames in various ways
        1) From CSV file
        2) From excel file
        3) From Python Dictionary
        4) From List of Tuples
        5) From List of Dictionary 
'''

'''
    From CSV file
    -------------
    Panda provides 'read_csv()' method to read the data from csv and create a dataframe
    NOTE: we can pass few more parameters along with name. explore it later
'''
dataFrame = pd.read_csv("/Users/ycs/PycharmProjects/PythonTutorial/data/Salary_Data.csv")

'''
    From excel file
    -------------
    Panda provides 'read_excel()' method to read the data from csv and create a dataframe
    NOTE: we can pass few more parameters along with name. explore it later
'''
dataFrame = pd.read_excel("/Users/ycs/PycharmProjects/PythonTutorial/data/Salary_Data.xlsx", "Sheet1")

'''
    From Python Dictionary
    ----------------------
    Panda provides DataFrame constructor to create dataframe from data in variable.
'''
data = {
    'name' : ['yatish','ramya'],
    'age' : [27, 35]
}
dataFrame1 = pd.DataFrame(data)

'''
    From List of Tuples
    -------------------
    Panda provides DataFrame constructor to create dataframe from data in variable.
'''
data1 = [
            ('yatish',27),
            ('ramya',35)
        ]
dataFrame2 = pd.DataFrame(data1, columns = ['name','age'])

'''
    From List of Dictionary
    -----------------------
    Panda provides DataFrame constructor to create dataframe from data in variable.
'''
data2 = [
            {'name' : 'yatish', 'age' : 27},
            {'name' : 'ramya', 'age' : 35}
        ]
dataFrame3  = pd.DataFrame(data2)

'''
Specifying the index of the rows manually. Usually, 1st Row will be given index 0 and 2nd
Row with index 1. In below code we are explicitly mentioning that make 1st rows as index 1
and 2nd row as index 0
'''
dataFrame4 = pd.DataFrame(data2, index=[1,0])


'''
    DataFrame contains 'shape' property which gives the dimension, i.e. row,column of the data frame.
'''
dimensionTuple = dataFrame.shape # dimensionTuple value is (30,2). which is a tuple
row, column = dataFrame.shape   # if we want row and column in separate variables then assigning variables should be
                                #    like this rowVariable, ColumnVariable. 'row' value is 30 and 'column' value is 2


'''
    DataFrame contains 'head()' function which returns dataFrame of only top few rows. by default 5 rows.
    We can alter the default number 5 to any number by passing it as parameter to 'head()'
'''
headDataFrame = dataFrame.head()
headDataFrame1 = dataFrame.head(10)


'''
    Similarly like 'head()' function, DataFrame contains 'tail()' function as well.
'''
tailDataFrame = dataFrame.tail()
tailDataFrame1 = dataFrame.tail(10)


'''
    Getting dataFrame of specified custom rows
'''
rowsDataFrame = dataFrame[3:10] # This will return data frame of 3rd to 10th row. here 3 and 10 are row numbers,
                                # 3 is inclusive and 10 is exclusive. remember rows start from 0 not 1.


'''
    Getting the column header names
'''
columns = dataFrame.columns # columns --> Index(['YearsExperience', 'Salary'], dtype='object')


'''
    We saw how to get rows of the data frame. Now lets see how to get only specific column data
'''
yearsExperienceColumnData = dataFrame.YearsExperience # it returns complete column data of 'YearsExperience'.
                                                      # The data type is 'Series'
yearsExperienceColumnData1 = dataFrame['YearsExperience'] # This is one more way. we can specify withing []

multipleColuns = dataFrame[['YearsExperience', 'Salary']] # Returning Multiple columns. Return type is not
                                                          # 'Series', if it is more than one column then 
                                                          # it return 'DataFrame' type.
                                                          # NOTE: columns within double [[]] not []

'''
    mathematical functions like min,max etc.
    
    If you want get all statistics like min,max,mean,count etc at once then you can use 'describe()' function of data 
    frame. It will give you count,min,max,mean,standard deviation, 25% percentile, 50% percentile, 75% percentile.
'''
maxValue = dataFrame['YearsExperience'].max()
minValue = dataFrame['YearsExperience'].min()
meanValue = dataFrame['YearsExperience'].mean()
standardDeviationValue = dataFrame['YearsExperience'].std()
columnStats = dataFrame['YearsExperience'].describe()
dataFrameStats = dataFrame.describe()


'''
    SQL like support on data frames.
'''
dfMoreThanFiveYearExp = dataFrame[dataFrame.YearsExperience > 5] # SELECT * FROM dataFrame
                                                                 # WHERE YearsExperience > 5
salColumnMoreThanFiveYearExp = dataFrame['Salary'][dataFrame.YearsExperience > 5] # SELECT Salary FROM dataFrame
                                                                                  # WHERE YearsExperience > 5

'''
    How to get rows of the data based on the index?
        Using 'loc' or 'iloc' methods.
        
    What is the difference between 'loc' and 'iloc'?
        'loc' accepts only row specifications, we cannot give columns which we want. It accepts either integer or string.
        'iloc' accepts both row and column specification, we can give columns. It accepts only integers not string.
        
        eg: dataFrame.loc[0:5] --> Works
            dataFrame.loc[0:5, 1] --> Error. we cannot specify columns specification. it gives rows data with all columns.
            dataFrame.iloc[0:5, 1] --> Works
            dataFrame.iloc[0:5] --> Works
            dataFrame.loc['indexabc'] --> Works
            dataFrame.iloc['indexabc'] --> Error. 'iloc' doesn't accept strings, it accepts only integers.
            
'''
firstRow = dataFrame.loc[0]
firstToFifthRow = dataFrame.loc[0:5]
firstToFifthRowWithOnlySalCol = dataFrame.iloc[0:5, 1]

'''
    you know that, pandas will give a index to the data frame implicitly which is an integer index from 0 to n.
    We can set any column of the data frame as the index instead of implicit index provided by pandas.
    
    In below example, we are using 'Salary' column as the index, it is not unique and can have duplicate values?
        That's ok. even if the column have duplicate values also. If duplicate values are there then pandas will bring
        in it's implicit index 0 to n to identify each row uniquely along with 'Salary' column. So basically we have 2 
        indexes once is implicit one and 'Salary' column. we can have any other string column as well as index, it need
        not be numbers only.
        
    What is the advantage of making a column of our data as index?
        Consider if we query data frame most of the time on a column, then it is better to make it an index column so that
        we can easily get the data using 'loc' instead of SQL way of querying.
        eg:
            consider, student data, we usually will be trying to get data of a student using his roll numbers. rather than
            running 'dataFrame[dataFrame.rollNumbner = 5]' we can run 'dataFrame.loc[5]' which is more efficient.
            
    Consider if you make a column 'name' as index, and there are 5 rows with name 'yaitsh' then what happens on running
    'dataFrame.loc['yatish']'?
        It will return us all 5 rows with 'name' value as 'yatish'. It doesn't give any error.
'''
salIndexDataFrame = dataFrame.set_index('Salary') 
customRow = salIndexDataFrame.loc[54445]
dataFrame.set_index('Salary', inplace=True) # 'inplace' makes it set the index in 'dataFrame' only instead of returning 
                                            # data frame with index as 'Salary'








