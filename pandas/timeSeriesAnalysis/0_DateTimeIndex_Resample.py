'''

What is Time series?
    Time series is a set of data points indexed in time order.

'''

import pandas as pd

# This is the stock market details of 'Apple' company shares.
data = {
    'timestamp' : [pd.Timestamp(year=2019, month=11, day=2, hour=12, minute=30, second=45),
                   pd.Timestamp(year=2019, month=11, day=3, hour=12, minute=30, second=45),
                   pd.Timestamp(year=2019, month=11, day=4, hour=12, minute=30, second=45),
                   pd.Timestamp(year=2019, month=11, day=5, hour=12, minute=30, second=45),
                   pd.Timestamp(year=2019, month=11, day=6, hour=12, minute=30, second=45),
                   pd.Timestamp(year=2019, month=10, day=6, hour=12, minute=30, second=45),
                   pd.Timestamp(year=2019, month=10, day=6, hour=12, minute=30, second=45)],
    'open' : [10, 20, 30, 40, 50, 60, 70],
    'high' : [25, 35, 45, 55, 65, 75, 85],
    'low' : [5, 15, 25, 35, 45, 55, 65],
    'close' : [7, 17, 27, 37, 47, 57, 67],
    'volume' : [1000, 2000, 3000, 4000, 5000, 6000, 7000]
}


dataFrame = pd.DataFrame(data)
dataFrame.set_index('timestamp', inplace=True)

dataFrame['2019-11-2']  # It will give us all rows with data '2019-11-2'.
                        # Basically, it will give all rows of Nov 2nd 2019.
dataFrame['2019-11']  # It will give us all rows with data '2019-11'.
                      # Basically, it will give all rows of Nov complete month 2019.
dataFrame['2019-11-2' : '2019-11-4'] # It will give us all rows from date 2nd Nov 2019
                                     # to 4th Nov 2019
                      
dataFrame['2019-11'].close.mean() # Gives us mean of all the close values in Nov month 2019

dataFrame.close.resample('M').mean() # Gives the mean of each month of the data frame. 'M' specifies monthly.
# Output --> timestamp
#           2019-10-31    62
#           2019-11-30    27
#           Freq: M, Name: close, dtype: int64
# As shown in the above output, The dataFrame have only Oct and Nov data in data frame. So it give us
# mean of 'close' values of each month Oct and Nov. If June data was present in data frame then there
# would have been one more row for June along with Oct and nov.
# We can specify 'W' to specify 'Weekly', 'D' to specify 'Daily','Y' to specify 'Yearly' and 
# 'Q' for Quaters of year. Lot of other values are supported, Check the Doc for it.
                                    
                             

                             







