import pandas as pd

data=pd.read_csv(r'C:\Users\admin\Downloads\archive (5)\netflix.csv')

new =data["duration"].str.split(" ",n=1,expand=True)
data.dropna()

data["duration"]=new[0]

data["Minutes"]=new[1]

print(data["duration"])
print(data["Minutes"])


