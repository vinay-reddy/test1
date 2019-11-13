import pandas as pd
import json

df = pd.read_json('/Users/vinayreddy/Desktop/logs/json/4500.json')

pd.options.display.max_rows = 1200000
pd.options.display.max_colwidth = 1000000

for i in range(len(df['devices']['device'])):
    for j in range(len(df['devices']['device'][i]['details'][0]['entry'])):
        if 'value' in df['devices']['device'][i]['details'][0]['entry'][j]:
            continue
        else:
#            print(df['devices']['device'][i]['details'][0]['entry'])
            print(df['devices']['device'][i])

