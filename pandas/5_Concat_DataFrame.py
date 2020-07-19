'''
 We can concatinate data frames using 'concat()'
'''

import pandas as pd

data1 = {
    'City' : ['Delhi', 'Karnataka','Kerala'],
    'Temperature' : [10,20,30],
    'Population' : [100, 200, 300]
}

data2 = {
    'City' : ['Frankfurt', 'Berlin','Singen'],
    'Temperature' : [40,50,60],
    'Population' : [400, 500, 600]
}

dataFrame1 = pd.DataFrame(data1)
dataFrame2 = pd.DataFrame(data2)

concatinatedDataFrame = pd.concat([dataFrame1, dataFrame2])  # This will append the rows of 'DataFrame2' to 'DataFrame1'
# Output -->      City       Temperature  Population
#           0      Delhi           10         100
#           1  Karnataka           20         200
#           2     Kerala           30         300
#           0  Frankfurt           40         400
#           1     Berlin           50         500
#           2     Singen           60         600
concatinatedDataFrame1 = pd.concat([dataFrame1, dataFrame2], ignore_index=True) # In the above output, you can see that
                                                                                # index value re-starts from 0 again. If
                                                                                # we specify 'ignore_index=True' then
                                                                                # it will be re-indexed from 0 to end.
# NOTE : If there is a miss match in the columns of 2 data frames, then the missing values will be filled with 'NaN'


concatinatedDataFrame2 = pd.concat([dataFrame1, dataFrame2], keys=['India','Germany']) # Basically this will assign
# Output --> India      0      Delhi           10         100
#                       1  Karnataka           20         200
#                       2     Kerala           30         300
#           Germany     0  Frankfurt           40         400
#                       1     Berlin           50         500
#                       2     Singen           60         600                          # 'India' as key to dataFrame1
                                                                                       # 'Germany' as key to dataFrame2
# Internally it will be like index (India,0), (India,1), (India,2), (Germany,0), (Germany,1) and (Germany,2).


IndiaDF = concatinatedDataFrame2.loc["India"]       # This will fetch DF with index 'India'
# Output -->         City       Temperature  Population
#               0     Delhi           10         100
#               1     Karnataka       20         200
#               2     Kerala          30         300


data3 = {
        'City' : ['Bangalore','Mysore'],
        'Temperature' : [27,25]
        }

data4 = {
        'City' : ['Mysore', 'Bangalore'],
        'Population' : [9000,3000]
        }    

dataFrame3 = pd.DataFrame(data3)
dataFrame4 = pd.DataFrame(data4)                                                                          
          
concatinatedDataFrame3 = pd.concat([dataFrame3,dataFrame4])                                                                
# Output -->         City          Population  Temperature
#               0   Bangalore         NaN         27.0
#               1   Mysore            NaN         25.0
#               0   Mysore            3000.0      NaN
#               1   Bangalore         9000.0      NaN

# We need the 'Temperature' to be added to same rows. instead of creating another row with 'Temperature' as 'NaN'.
# By Default 'axis' is 0. if we set it to 'axis=1' then add duplicate column 'City' and then show it in same row
concatinatedDataFrame4 = pd.concat([dataFrame3,dataFrame4], axis=1)
# Output -->    City        Temperature       City      Population
#           0   Bangalore         27       Mysore            9000
#           1   Mysore            25       Bangalore         3000


# We can concatinate 2 or more data frames.
concatinatedDataFrame5 = pd.concat([dataFrame1,dataFrame2,dataFrame3,dataFrame4])
'''
How can i concatinate without getting duplicate 'City' column?
    Can doing it using 'merge' instead of 'concat'
'''


'''
Similarly like how we can concatinate 2 or more data frames. We can concatinate data frame and Series.
'''
temperatureSeries = pd.Series([9000,3000], name='Population')
concatinatedDataFrame6 = pd.concat([dataFrame3,temperatureSeries])
# Output -->        City        Temperature       0
#           0    Bangalore         27.0         NaN
#           1     Mysore           25.0         NaN
#           0        NaN           NaN          9000.0
#           1        NaN           NaN          3000.0
# As we can see it added the series as row which doesn't make any sense. we need to add it as column as shown below,
concatinatedDataFrame7 = pd.concat([dataFrame3,temperatureSeries], axis=1)
# Output -->        City        Temperature     Population
#               0  Bangalore         27           9000
#               1   Mysore           25           3000

