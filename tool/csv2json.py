import csv
import json
import pandas as pd
import shutil
from datetime import datetime
from typing import List, Dict


def process_patients() -> List:
    df = pd.read_csv("jokyo20200320-0.csv", index_col=0)

    # 集計用にコピーします(deepcopyの方がいいかな？)
    df_summary = df
    print(df_summary.groupby('判明日').count()\
            .drop(['性別', '居住地', '現状'], axis=1).rename(columns={'年代':'count'}) )
    new_df = df.rename(columns={'判明日':'リリース日', '現状':'退院'})
    new_df['date'] = new_df['リリース日'] #.replace('(.*)/(.*)/(.*)', r'\1-\2-\3', regex=True)
    new_df['退院'].mask(new_df['退院'] == '退院', '○', inplace=True)
    new_df['退院'].mask(new_df['退院'] != '○', '', inplace=True)
    #print(new_df)
    json_data = json.loads(new_df.T.to_json(force_ascii=False))

    # DataFrameのjson出力を加工
    print(json_data)
    patients = []
    for jd in json_data:
        # この辺りdataframeで一括で変えられるなら変えたい
        json_data[jd]['リリース日'] = datetime.strptime(json_data[jd]['リリース日'],\
                '%Y/%m/%d').strftime('%Y-%m-%dT08:00:00.000Z')
        json_data[jd]['date'] = datetime.strptime(json_data[jd]['date'],\
                '%Y/%m/%d').strftime('%Y-%m-%d')
        patients.append(json_data[jd])
    
    return patients


def process_inspections_summary() -> Dict:
    inspections_summary = {}
    patients_summary = []
    df = pd.read_csv("kensa20200320-0.csv")
    print(df.head)
    
    patients_summary_data = df[["検査日","陽性確認者数"]]
    pat_dat = patients_summary_data.rename(columns={"検査日":"日付", "陽性確認者数":"小計"})
    pat_json = json.loads(pat_dat.to_json(force_ascii=False))

    inspection_summary_data = df[["検査日","検査数（延べ人数）"]]
    ins_dat = inspection_summary_data.rename(columns={"検査日":"labels", "検査数（延べ人数）":"県内"})
    ins_json = json.loads(ins_dat.to_json(force_ascii=False))
    
    date = []

    patient_counts = []
    for ij in ins_json["県内"]:
        patient_counts.append({ "日付":pat_json["日付"][ij], "小計":pat_json["小計"][ij] })

    inspection_counts = []
    for ij in ins_json["labels"]:
        ild = datetime.strptime(ins_json["labels"][ij],'%Y/%m/%d').strftime("%m\/%d")
        date.append(ild)
    for ij in ins_json["県内"]:
        inspection_counts.append(ins_json["県内"][ij])
    
    inspections_summary = {
        "date": "2020\/03\/10 11:00",
        "data": {
            "県内": inspection_counts
        },
        "labels": date
    }
    patients_summary = {
        "date": "2020\/03\/10 11:00",
        "data": patient_counts
    }
    return patients_summary, inspections_summary


patients = process_patients()
patients_summary, inspections_summary = process_inspections_summary()

result = {
    "contacts": {
        "date": "2020/03/10 10:00",
        "data": []
    },
    "querents": {
        "date": "2020/03/09 10:10",
        "data": []
    },
    "patients": {
        "date": "2020/03/10 19:00",
        "data": patients
    },
    "discharges_summary": {
        "date": "2020/03/10 19:00",
        "data": []
    },
    "inspections": {
        "date": "2020/03/10 11:00",
        "data": []
    },
    "patients_summary": patients_summary,
    "inspections_summary": inspections_summary,
    "better_patients_summary": {
        "date": "2020/03/10 19:00",
        "data": {}
    },
    "lastUpdate": "2020/03/12 19:30",
    "main_summary": {
        "attr": "検査実施人数",
        "value": 0,
        "children": [
            {
                "attr": "陽性患者数",
                "value": 0,
                "children": [
                    {
                        "attr": "入院中",
                        "value": 0,
                        "children": [
                            {
                                "attr": "軽症・中等症",
                                "value": 0
                            },
                            {
                                "attr": "重症",
                                "value": 0
                            }
                        ]
                    },
                    {
                        "attr": "退院",
                        "value": 0
                    },
                    {
                        "attr": "死亡",
                        "value": 0
                    }
                ]
            }
        ]
    }
}
#print(patients)
#print(inspections_summary)

# create backup
shutil.copy('../data/data.json', 'data.json.bak')
with open('../data/data.json', 'w') as f:
    json.dump(result, f, ensure_ascii=False, indent=4)

print("Done.")
