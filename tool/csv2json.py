import csv
import json
import pandas as pd
from datetime import datetime

#def read_csv(file_name):
#    with open(file_name, "r") as f:
#        reader = csv.reader(f)
#        l = [row for row in reader]
#    print(l)


#read_csv("jokyo20200317-0.csv")

df = pd.read_csv("jokyo20200317-0.csv", index_col=0)

# 集計用にコピーします(deepcopyの方がいいかな？)
df_summary = df
print(df_summary.groupby('判明日').count()\
        .drop(['性別', '居住地', '現状'], axis=1).rename(columns={'年代':'count'}) )
new_df = df.rename(columns={'判明日':'リリース日', '現状':'退院'})\
        .replace('(.*)/(.*)/(.*)', r'\1-\2-\3', regex=True)

new_df['date'] = new_df['リリース日']
new_df['退院'].mask(new_df['退院'] == '退院', '○', inplace=True)
new_df['退院'].mask(new_df['退院'] != '○', '', inplace=True)
print(new_df)
json_data = json.loads(new_df.T.to_json(force_ascii=False))

# DataFrameのjson出力を加工
print(json_data)
result = []
for jd in json_data:
    result.append(json_data[jd])

print(result)
