# Need

- Python3
- pip

# Usage

```sh
$ pip install -r requirements.txt --target .
$ python3 crawl_shingatacoronavirus.py
$ cat patients_20200409.csv (change 20200409 to target day)  
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

