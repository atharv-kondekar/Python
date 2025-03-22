import pandas as pd
import numpy as np

array=np.arange(0,20).reshape(5,4)

#creating the DataFrame 

data=pd.DataFrame(
    data=array,
    index=["Row1","Row2","Row3","Row4","Row5"],
    columns=["Column1","Column2","Column3","Column4"]
)

print(data)
print("\n",type(data))

print(data.head(2)) # Gives The First 2 rows 
print(data.tail(2)) # Gives The Last 2 rows 