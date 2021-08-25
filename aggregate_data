import pandas as pd
import os

df = pd.read_csv('.\\statsgg\\ebomberr.csv.csv')

# creating empty dataframe
total_data = pd.DataFrame()

files = [file for file in os.listdir('.\\statsgg')]

for file in files:
    df = pd.read_csv(f'.\\statsgg\\{file}')
    total_data = pd.concat([total_data, df])

total_data.to_csv("totaldata.csv", index=False)

new_data = pd.read_csv('totaldata.csv')


new_data = new_data.drop(columns=['Unnamed: 0'])
print(new_data)
