# Need

- Python3
- pip
- Java8(required by tika PDF reader)

# Usage

```sh
$ pip install -r requirements.txt --target .
$ python3 crawl_shingatacoronavirus.py
$ cat patients_20200409.csv (change 20200409 to target day)  
$ python3 get_from_jokyo_pdf.py
$ cat list20200409.csv
$ python3 csv2json.py
$ sed -i '' s'/\\\\/\\/g' data.json
$ vim data.json
Change 検査実施人数's value
"main_summary": {
        "attr": "検査実施人数",
        "value": 1000 <- 
$ cp data.json ../data/data.json
```

# tool

## crawl_shingatacoronavirus.py

 * [感染確認状況や関連情報](http://www.pref.saitama.lg.jp/a0701/shingatacoronavirus.html)から陽性確認者数をスクレイピングし、CSVファイルに書き出すスクリプトです。

以下の手順でスクリプトを実行します。

```sh
$ # 引数なしの場合は「patients_20200408.csv」のような現在の日時を含んだCSVファイルを生成します。
$ python crawl_shingatacoronavirus.py
$
$ # 引数を指定した場合は、patients_<YYYYMMDD>.csv」のようなCSVファイルを生成します。
$ # (フォーマットがYYYYMMDDでない場合は、現在の日時を含んだCSVファイルを生成します)
$ python crawl_shingatacoronavirus.py 20200409
$
$ # 以下のようなCSVファイルが生成されます。
$ cat patients_20200408.csv
253,213,205,8,35,5
```

