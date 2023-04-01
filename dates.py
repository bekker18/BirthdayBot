import pandas as pd

df = pd.read_excel('file.xlsx', engine='openpyxl')

df.iloc[:, 1:3] = df.iloc[:, 1:3].astype(str)

df['new_column'] = df.iloc[:, 1:3].apply(lambda x: '/'.join(x), axis=1)

dictionary = dict(zip(df.iloc[:, 0], df['new_column']))
dictionary = {value:key for key, value in dictionary.items()}
