'''
Consider, if the data doesn't have the dates in it. Then we can generate the dates using 'date_range' function.
'''

import pandas as pd

# This is the stock market details of 'Apple' company shares.
data = {
    'open' : [10, 20, 30, 40, 50, 60, 70],
    'high' : [25, 35, 45, 55, 65, 75, 85],
    'low' : [5, 15, 25, 35, 45, 55, 65],
    'close' : [7, 17, 27, 37, 47, 57, 67],
    'volume' : [1000, 2000, 3000, 4000, 5000, 6000, 7000]
}
dataFrame = pd.DataFrame(data)

# In above 'data', it doesn't have any dates associated with the 'Apple' company stock market data. Say like we know
# from which date to what date was this data taken. 
dateRange = pd.date_range(start='10/23/2019', end='10/31/2019', freq='B') # freq='B' means 'Bussiness Days'
                                                                          # it basically, excludes weekend dates
                                                                          # '10/26/2019' and '10/27/2019'

dataFrame1 = dataFrame.set_index(dateRange)

# If you don't know the end date or you find it difficult to find. Then instead of end date, you can specify 'periods'
# basically same as number of rows of data present.
dateRange2 = pd.date_range(start='10/23/2019', periods=7, freq='B') # it is equivalent to 'end='10/31/2019''

dataFrame2 = dataFrame.set_index(dateRange2)







