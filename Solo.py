import pandas as pd
df=pd.read_csv('https://sololearn.com/uploads/files/titanic.csv')
small_df=df[['Age','Sex']]
arr=df[['Pclass', 'Fare', 'Age']].values



print(arr[:,:])