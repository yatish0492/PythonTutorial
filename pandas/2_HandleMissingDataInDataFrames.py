'''

In the data we get, there will be some missing data. We need to fill them with some value which makes it easier for us to
run any analytics on the data.

'''
import pandas as pd

dataFrame = pd.read_csv("/Users/ycs/PycharmProjects/PythonTutorial/data/Salary_Data.csv")


# We can fill the missing data (NaN) with anything else using '.fillna()'
df1 = dataFrame.fillna(0)
df2 = dataFrame.fillna('empty')


# Sometimes say we have string column. filling missing data with 0 doesn't make sense but for integer columns you want
# 0. Then you can do it by passing a dictionary instead of a single value.
df3 = dataFrame.fillna({
    'YearsExperience' : 0,
    'Salary' : 0,       # fills missing data in 'Salary' column with 0
    'Name' : 'No Name'  # fills missing data in 'Name' column with 'No Name'
})


# Sometimes just filling missing value with 0 is not correct. so we can decide what value should be filled in that case
# Consider, if the column is 'Temperature' and we don't know the temperature and put is as 0, that means it was 0 degree
# on that day, which is not correct. so in this case we can assign previous day temperature to missing data day.
df4 = dataFrame.fillna(method='ffill')    # 'ffill' stands for forward fill. this method will fill the missing values
                                          #   with previous row value.

df5 = dataFrame.fillna(method='bfill')    # 'bfill' stands for backward fill. this method will fill the missing values with
                                          #   next row value.

df6 = dataFrame.fillna(method='ffill', axis='index') # 'axis' specifies whether the 'method' should be applied
                                               # horizontally(Row) or vertical(Column). by default value is 'columns'.
                                               # 'index' stands for horizontal(Row).

df7 = dataFrame.fillna(method='ffill', limit=1)   # 'limit' specifies like say if 2 consecutive rows of the column have
                                            #  missing data then both of them will be filled with previous row data.
                                            #  If limit value is '1' then only 1st of the 2 consecutive rows will be
                                            #  filled and 2nd one will be left as 'NaN'
# There are lot of other methods and parameters, you can see it in documentation.



# there is one more method 'interpolate()' for data frames. Please study how 'interpolate' works it is similar to
# linear regression etc.
df8 = dfdataFrame.interpolate()     # By default 'method' will be 'linear' there are many other methods that we can specify.
df9 = dataFrame.interpolate(method='quadratic') # we are overriding 'method' from linear to 'quadratic'.



# 'dropna()', this method will take out all the rows with missing data(NaN)
droppedNaDF = dataFrame.dropna() # This will drop the rows even if any once column value is missing(NaN)
droppedNaAllDF = dataFrame.dropna(how='all') # This will drop the row only if all the column values are missing(NaN).
                                             # If any one of the column value is not missing then it won't remove it.
df10 = dataFrame.dropna(thresh=1)   # 'thresh' stands for threshold. it will retain rows which has atleast 1 non
                                    #  missing(NaN) value. If thresh=2, then it will retain rows which have atleast
                                    #  2 non missing(NaN) values, others will be filtered out.
# NOTE : If we have make any column of our data as index. then that value will not considered for 'thresh' or in
#        'dropna'. we cannot consider that like, ok, we have one non-missing(NaN) value in the row.



# 'replace()', this method can be used to replace any value with any custom value.
df11 = dataFrame.replace(54445, 00000)              # Replace any column value '54445' with '00000'
df12 = dataFrame.replace('Yaitsh', 'Yatish C S')    # Replace any column value 'Yaitsh' with 'Yatish C S'
import numpy as np              # 'NaN' is not present in pandas, it is present in 'numpy' so importing it.
df13 = dataFrame.replace(-9999, np.NaN)     # Replace any column value '-9999' with missing-data(NaN)
df14 = dataFrame.replace([-9, -99, -999], np.NaN)   # Replace any column value '-9' or '-99' or '-999' with missing-data(NaN)
df15 = dataFrame.replace({
    'YearsExperience' : -9,
    'Salary' : -99,
    'Name' : 'No Name'
}, np.NaN)                  # Replace '-9' in column 'YearsExperience', '-99' in column 'Salary' and 'No Name' in column
                            # 'Name' with missing-data(NaN)
df16 = dataFrame.replace({
    -9 : np.NaN,
    -99 : np.NaN,
    'No Name' : np.NaN,
    'Yaitsh' : 'Yatish C S'
})                          # Same as above but we are not specifying based on column. we are just mentioning what value
                            # in any column needs to be replaced with what value.

df17 = dataFrame.replace('[A-Za-z]','This is String', regex=True)   # We can use regex as well. but need to set flag
df18 = dataFrame.replace('*yatish*', 'Yatish C S', regex=True)      # 'regex=True'
df19 = dataFrame.replace({
    'YearsExperience' : [0-5],
    'Salary' : [0-5],
    'Name' : '[A-Za-z]'
}, np.NaN, regex=True)

df20 = dataFrame.replace(['Engineer','Doctor','Lawyer'],[1,2,3]) # This will replace 'Enginner' with 1
                                                                 # 'Doctor' with '2' and 'Lawyer with 3.
                                                                 # We will use this more in data science
                                                                 # as we need these categories as number 
                                                                 # representation.















