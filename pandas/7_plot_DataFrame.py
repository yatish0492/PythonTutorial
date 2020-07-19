'''

'plot()' is used to plot graphs for the Numeric columns of the data frame.

'''

import pandas as pd

data = {
    'Country' : ['India', 'Germany','America'],
    'Temperature' : [10,20,30],
    'Population' : [100, 200, 300]
}

dataFrame = pd.DataFrame(data)

dataFrame.plot()

dataFrame.plot(kind='bar') # We can specify which kind of chart using 'kind' parameter.


