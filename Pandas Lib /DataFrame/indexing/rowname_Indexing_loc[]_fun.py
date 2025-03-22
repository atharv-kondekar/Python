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
          Column1  Column2  Column3  Column4  Column5
Row1        0        1        2        3        4
Row2        5        6        7        8        9
Row3       10       11       12       13       14
Row4       15       16       17       18       19
Row5       20       21       22       23       24
Row6       25       26       27       28       29
"""

print("\n The 1st row data : ")
print(Data.loc["Row1"])

print("\n\n The Row 1,3,5 Data : ")
print(Data.loc[["Row1","Row3","Row5"]])