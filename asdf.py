import pandas as pd
import json

df = pd.read_json('/Users/vinayreddy/Desktop/logs/json/4500.json')


pd.options.display.max_rows = 1200000
pd.options.display.max_colwidth = 1000000

#print(df['devices']['device'][0].keys())

#print(df['devices']['device'][:])

for i in range(len(df['devices']['device'])):
#    print(df['devices']['device'][i]['model'] + "      "+  df['devices']['device'][i]['platform'])
#    a = print(df['devices']['device'][i]['details'][0]['entry'])
#    if 'Android' in df['devices']['device'][i]['platform']:
#        print(df['devices']['device'][i])
#    print(df['devices']['device'][0].keys())

    for j in range(len(df['devices']['device'][i]['details'][0]['entry'])):
        if 'value' in df['devices']['device'][i]['details'][0]['entry'][j]:
            continue
        else:
            print(df['devices']['device'][i]['details'][0]['entry'])




# fh = open('/Users/vinayreddy/Desktop/logs/json/4500.json', 'r')
#
# json_read = json.load(fh)
# for keys in json_read.keys():
#     print(keys)
# #df['devices']
#
# for key in json_read['devices'].keys():
#     print(key)
#
#
#
# print(type(json_read['devices']['device']))
#
#
# print(dict(json_read['devices']['device']))
#
#
# fh.close()
