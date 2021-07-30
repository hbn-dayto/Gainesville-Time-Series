import os
import pandas as pd
import numpy as np
import csv

from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates
from pandas.io.parsers import read_csv

plt.style.use('seaborn')

# Adds padding to plot
plt.tight_layout()

# Shows plot
plt.show()

df = pd.read_csv('zillow_data_zip.csv')
# print(df.head().T)

# print(df['RegionName'])
# print(df.loc[df[:, 'RegionName' == 32609]])


zip_codes = np.array([32609, 32653, 32606, 32605, 32607, 32608, 32641, 32601, 32603, 32611])

# zip_codes = [32609, 32653, 32606, 32605, 32607, 32608, 32641, 32601, 32603, 32611]
zip_codes.sort()


subset = df[df['RegionName'].isin(zip_codes)]
# print(subset.head())

subset.to_csv('gainesville_data.csv', sep = ',', header = "None", index = None)
zip_32608 = subset.iloc[0,9:]
print(zip_32608.head())

zip_32608.to_csv('32608.csv', index= 0, date = True,  sep = ',', header = "None")
zip_code1 = pd.read_csv('32608.csv')
print(zip_code1.index)
print(zip_code1.head())


# print(zip_codes)

# df_filter = df.query('RegionName == Gainesville')
# print(df_filter.head())

# df_filter = df[df['RegionName']] = 'Gainesville'
# print(df_filter.head())
# df_filter.to_csv('gainesville.csv', sep = '', header = "None", index = None)

# print(df_filter.shape())

# (x_values, y_values)
plt.ploto_date(data, y)