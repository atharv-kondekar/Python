import numpy as np
import pandas as pd

array=np.arange(0,30).reshape(6,5)

Data=pd.DataFrame(
    data=array,
    index=["Row1","Row2","Row3","Row4","Row5","Row6"],
    columns=["Column1","Column2","Column3","Column4","Column5",]
)

print(Data)
"""
op:
            0        1        2         3        4
          Column1  Column2  Column3  Column4  Column5
0    Row1        0        1        2        3        4
1    Row2        5        6        7        8        9
2    Row3       10       11       12       13       14
3    Row4       15       16       17       18       19
4    Row5       20       21       22       23       24
5    Row6       25       26       27       28       29
"""

print(Data.iloc[1:5,1:3],"\n")

print(Data.iloc[1:,1:3],"\n")

print(Data.iloc[:,:2],"\n")

print(Data.iloc[:,[0,4]],"\n")

print(Data.iloc[[1,4],:],"\n")