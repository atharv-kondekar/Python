import pandas as pd
from io import StringIO

string=( 'Col 1,Col 2,Col 3\n'
        'a,b,c\n'
        '1,3,10\n'
        '2,3,4'
        )
# This is the String Seprated by the ' Comma , '

df=pd.read_csv(StringIO(string),sep=',')
print(df)

#This String Seprated by the Tab 
string1=( 'Col 1        Col 2   Col 3\n'
        'a      b       c       \n'
        '1      3       10      \n'
        '2      3       4       '
)

df1=pd.read_csv(StringIO(string1),sep='\t')
print("\n",df1)