import pandas as pd
from io import StringIO

df=pd.read_csv("username.csv",sep=';')
print(df)
"""
    Username   Identifier First name Last name
0   booker12         9012     Rachel    Booker
1     grey07         2070      Laura      Grey
2  johnson81         4081      Craig   Johnson
3  jenkins46         9346       Mary   Jenkins
4    smith79         5079      Jamie     Smith
"""

#Now I Just want "Username" & "First name" column 

df1=pd.read_csv("username.csv",sep=';',usecols=['Username','First name'])
print("\n\t ---- The Two Cloumns You want --------\n",df1)