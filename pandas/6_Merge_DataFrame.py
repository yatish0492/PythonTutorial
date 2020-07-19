'''
    Merge is also similar to 'concat' but it doesn't give duplicate column. it is like 'join' in SQL.
    
    Merge accepts only 2 data frames. we cannot give more than 2 data frames to merge.
'''

import pandas as pd

data1 = {
    'City': ['Bangalore', 'Mysore'],
    'Temperature': [27, 25]
}

data2 = {
    'City': ['Mysore', 'Bangalore'],
    'Population': [9000, 3000]
}

dataFrame1 = pd.DataFrame(data1)
dataFrame2 = pd.DataFrame(data2)

concatinatedDataFrame1 = pd.merge(dataFrame1, dataFrame2, on='City') # we need to specify 'on' column.
# Output -->     City        Temperature     Population
#          0   Bangalore          27          3000
#          1     Mysore           25          9000


'''
    What happens if the values of 'City' column doesn't match.
'''
data3 = {
        'City' : ['Bangalore','Mysore', 'Kolar', 'Hasan'],
        'Temperature' : [27, 25, 28, 29]
        }

data4 = {
        'City' : ['Mysore', 'Bangalore', 'Hubli', 'Sakleshpur'],
        'Population' : [9000, 3000, 5000, 2000]
        }    

dataFrame3 = pd.DataFrame(data3)
dataFrame4 = pd.DataFrame(data4)                                                                          
          
concatinatedDataFrame2 = pd.merge(dataFrame3,dataFrame4, on='City')
# Output-->     City           Temperature  Population
#           0  Bangalore           27        3000
#           1   Mysore             25        9000
# If the values of both data frames doesn't match then, it will give only intersection of them and exclude others.
# In above example, it took only common values in both data frames 'Bangalore','Mysore' and ignored other rows,
# 'Kolar','Hasan','Hubli' and 'Sakleshpur'


'''
    If it gives only intersection. It doesn't work out. how to handle?
        Don't worry. we have Good news. we can specify, how to join using 'how' parameter.
         how = 'left' --> For left join(Intersection + Left remaining in DF)
         how = 'right' --> For Right join(Intersection + Right remaining in DF)
         how = 'outer' --> For Outer join (Intersection + Left remaining in DF + Right remaining in DF)
      
    NOTE : By Default, the value of 'how' is 'inner'
'''
concatinatedDataFrame3 = pd.merge(dataFrame3,dataFrame4, on='City', how='left')
# Output -->    City        Temperature  Population
#           0  Bangalore           27      3000.0
#           1     Mysore           25      9000.0
#           2      Kolar           28         NaN
#           3      Hasan           29         NaN

concatinatedDataFrame4 = pd.merge(dataFrame3,dataFrame4, on='City', how='right')
# Output -->    City    Temperature     Population
#       0   Bangalore         27.0        3000
#       1      Mysore         25.0        9000
#       2       Hubli          NaN        5000
#       3  Sakleshpur          NaN        2000

concatinatedDataFrame5 = pd.merge(dataFrame3,dataFrame4, on='City', how='outer')
# Output -->    City    Temperature  Population
#       0   Bangalore         27.0      3000.0
#       1      Mysore         25.0      9000.0
#       2       Kolar         28.0         NaN
#       3       Hasan         29.0         NaN
#       4       Hubli          NaN      5000.0
#       5  Sakleshpur          NaN      2000.0

concatinatedDataFrame6 = pd.merge(dataFrame3,dataFrame4, on='City', how='outer', indicator=True)
# Output -->    City   Temperature  Population      _merge
#       0   Bangalore         27.0      3000.0        both
#       1      Mysore         25.0      9000.0        both
#       2       Kolar         28.0         NaN   left_only
#       3       Hasan         29.0         NaN   left_only
#       4       Hubli          NaN      5000.0  right_only
#       5  Sakleshpur          NaN      2000.0  right_only
# 'indicator=True', will include 'merge' column, which will give details about whether if the row is present in both
# data frame or left_only or right_only

data5 = {
    'City' : ['Delhi', 'Karnataka','Bengaluru'],
    'Temperature' : [10,20,30],
    'Population' : [100, 200, 300]
}

data6 = {
    'City' : ['Bengaluru', 'Berlin','Singen'],
    'Temperature' : [40,50,60],
    'Population' : [400, 500, 600]
}

dataFrame5 = pd.DataFrame(data5)
dataFrame6 = pd.DataFrame(data6)
concatinatedDataFrame7 = pd.merge(dataFrame5,dataFrame6, on='City', how='outer')
# Output -->    City    Temperature_x  Population_x  Temperature_y  Population_y
#       0      Delhi           10.0         100.0            NaN           NaN
#       1  Karnataka           20.0         200.0            NaN           NaN
#       2  Bengaluru           30.0         300.0           40.0         400.0
#       3     Berlin            NaN           NaN           50.0         500.0
#       4     Singen            NaN           NaN           60.0         600.0
# If in both the data frames, there is same column, then it will give us 2 different columns suffixed with '_x' for
# left data frame and columns suffixed with '_y' for right data frame.


# We can give custom suffixes as well, using 'suffixes' parameter
concatinatedDataFrame7 = pd.merge(dataFrame5,dataFrame6, on='City', how='outer', suffixes=('_left','_right'))
# Output --> City  Temperature_left  Population_left  Temperature_right  Population_right
# 0      Delhi              10.0          100.0                NaN               NaN
# 1  Karnataka              20.0          200.0                NaN               NaN
# 2  Bengaluru              30.0          300.0                40.0             400.0
# 3     Berlin               NaN          NaN                  50.0             500.0
# 4     Singen               NaN          NaN                  60.0             600.0







                    

