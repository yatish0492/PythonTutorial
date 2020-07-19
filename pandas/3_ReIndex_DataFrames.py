'''

Reindex means, consider we already have a index and we can Reindex it with a new index.

'''

import pandas as pd

dataFrame = pd.read_csv("/Users/ycs/PycharmProjects/PythonTutorial/data/Salary_Data.csv")


'''
Consider, i have set the index as the dates of the information. In that say like we have few dates missing in the middle.
Consider, for the current scenario we needs the data for all continuous dates without any dates missing, in this case,
we can re-index with dates without any missing dates in between.

NOTE: For the missing dates, there will be new rows added with those dates but the complete row will be missing 
        data(NaN)
'''
dt = pd.date_range('01-01-2019','01-11-2019')
index = pd.DatetimeIndex(dt)
df1 = dataFrame.reindex(index)