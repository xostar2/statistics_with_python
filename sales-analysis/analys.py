import os
import pandas as pd
import json


df = pd.read_csv("data/sales_data.csv")
df.head()
# df.shape
# # (number_of_rows, number_of_columns)
print(f'\n total row :{df.shape[0]},total column :{df.shape[1]}')



os.makedirs('output',exist_ok=True)

#save in differente format 

#1 save in json format

df.to_json('output/sales_data.json',orient='records',indent=2)

df.to_excel('output/sales_data.xlsx',index=False)

df.to_csv('output/sales_data.csv',index=False)




# print("print current working directory",os.getcwd())

# data_path = "data/sales_data.csv"

# if(os.path.exists(data_path)):
#     print(f"data file exists: {data_path}")
# else:
#     print(f"data file does not exist at path: {data_path}")