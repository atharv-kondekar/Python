
"""
    Q) Mala Given Date Chi All Information Pahije 
"""

import time 

str=input("Enter the Date DD-MM-YYYY : ")

result=time.strptime(str,"%d %m %Y")

print(result)