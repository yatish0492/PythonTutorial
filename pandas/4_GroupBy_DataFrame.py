'''

We can do groupby on the column of a data frame so that it creates seperate groups for each unique value in that column.

'''


import pandas as pd

data = {
    'Country' : ['India','Paris','India','India','Paris'],
    'places' : ['Taj Mahal', 'Eifil Tower', 'Madikeri', 'Goa', 'Catacomb'],
    'Temperature' : [50, 30, 40, 20, 60]
}

dataFrame = pd.DataFrame(data)

groups = dataFrame.groupby('Country') # it will return type 'pandas.core.groupby.DataFrameGroupBy'. it basically creates
                                      # something like Map with key value pair. key will be the each value of 'Country'
                                      # column. Value will be the dataFrame of rows with corresponding country.
                                      # Equivalent to - SELECT * FROM dataFrame GROUP BY Country


for country, countryDF in groups :
    print("key : ", country)
    print("Value : ", countryDF)
# Output --> key :  India
#           Value :    Country     places
#                   0   India     Taj Mahal
#                   2   India     Madikeri
#                   3   India     Goa
#           key :  Paris
#           Value :    Country       places
#                   1   Paris       Eifil Tower
#                   4   Paris       Catacomb


IndiaGroupDF = groups.get_group('India')  # Gets data frame of rows with 'Country' column value as 'India'.

maxNumberDF = groups.max()
# Output -->        Country      places       Temperature
#                   India      Taj Mahal           50
#                   Paris      Eifil Tower         60
# It gives the max value of Integer/Numeric columns within each group. As in the output 50 is the max temperature of
# 'Temperature' column within 'India' group. similarly 60 for 'Paris'

meanNumberDF = groups.mean()
describedGroupsDF = groups.describe()

groups.plot() # Gives the plot of Temperature graphs. it gives 2 charts, one for 'India' and other for 'Paris'
              # Basically, it plots the lines in graph for all Integer/Numeric columns




