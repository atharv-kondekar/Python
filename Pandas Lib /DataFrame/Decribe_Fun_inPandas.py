import numpy as np
import pandas as pd

array=np.arange(0,30).reshape(6,5)

Data=pd.DataFrame(
    data=array,
    index=["Row1","Row2","Row3","Row4","Row5","Row6"],
    columns=["Column1","Column2","Column3","Column4","Column5",]
)

print(Data) 

print(Data.describe())

"""
op:-
         Column1    Column2    Column3    Column4    Column5
count   6.000000   6.000000   6.000000   6.000000   6.000000
mean   12.500000  13.500000  14.500000  15.500000  16.500000
std     9.354143   9.354143   9.354143   9.354143   9.354143
min     0.000000   1.000000   2.000000   3.000000   4.000000
25%     6.250000   7.250000   8.250000   9.250000  10.250000
50%    12.500000  13.500000  14.500000  15.500000  16.500000
75%    18.750000  19.750000  20.750000  21.750000  22.750000
max    25.000000  26.000000  27.000000  28.000000  29.000000
"""

# Count = Represents The Total Number of non Null values in "Column" 
# mean = Gives the average / mean of the "Column"
# std = measures the Standard Deviation of the Mean of the "Column"
# min = Gives the minimum value in the "Column"
# 25 % = represents first quartile in the "Column"
#      = 25% of the data falls below this value.
#   
# 50% = represents middle value in the "Column"
# 75% = 75% of the data falls below this value
# max = the largest value in the column 
