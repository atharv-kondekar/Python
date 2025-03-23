import pandas as pd
"""
username.csv  data : 

        Username; Identifier;First name;Last name
        booker12;9012;Rachel;Booker
        grey07;2070;Laura;Grey
        johnson81;4081;Craig;Johnson
        jenkins46;9346;Mary;Jenkins
        smith79;5079;Jamie;Smith

        ===== The Data is Seprated By the Semicolon ';' =======
"""
# If i write just like this 
df=pd.read_csv('username.csv')
print(df)
"""
-------- op -----------
  Username; Identifier;First name;Last name
0               booker12;9012;Rachel;Booker
1                    grey07;2070;Laura;Grey
2              johnson81;4081;Craig;Johnson
3               jenkins46;9346;Mary;Jenkins
4                  smith79;5079;Jamie;Smith

"""

# Now i Write like this 

df1=pd.read_csv('username.csv',sep=';')
print("\n",df1)

"""
--------------- op ------------------
    Username   Identifier First name Last name
0   booker12         9012     Rachel    Booker
1     grey07         2070      Laura      Grey
2  johnson81         4081      Craig   Johnson
3  jenkins46         9346       Mary   Jenkins
4    smith79         5079      Jamie     Smith
"""

# Because i write like this :- sep=';'