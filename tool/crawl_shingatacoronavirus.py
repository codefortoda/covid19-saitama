# Save csv data from shingatacoronavirus.html page to file
# Usage
#    $ python3 crawl_shingatacoronavirus.py
#    $ python3 crawl_shingatacoronavirus.py 20200330

import re
import requests
import sys
from bs4 import BeautifulSoup as bs4
from datetime import datetime as dt

# 「感染確認状況や関連情報」(埼玉県)のWebサイトからHTMLを取得する。
res = requests.get('http://www.pref.saitama.lg.jp/a0701/shingatacoronavirus.html')

# 欲しい情報は「<div class="outline">...</div>」タグ内にあるので、改行を除去し、一行の文字列として抜き出す。
text = bs4(res.content, 'html.parser').select('.outline')[0].get_text().replace('\n', '')

# 必要な値を切り出す。「陽性確認者数」などの切り出し時のキーワードとして用いている文字列は
# 変更される可能性があり、その際の変更箇所把握を容易にするため、値ごとに正規表現を適用する。
m1 = re.search(r'陽性確認者数：([0-9]+)人', text).group(1)
m2 = re.search(r'現在の患者数：([0-9]+)人', text).group(1)
m3 = re.search(r'うち軽症・中等症：([0-9]+)人', text).group(1)
m4 = re.search(r'重症者：([0-9]+)人', text).group(1)
m5 = re.search(r'退院：([0-9]+)人', text).group(1)
m6 = re.search(r'死亡：([0-9]+)人', text).group(1)

# 検査数取得
text = bs4(res.content, 'html.parser').select('.outline')[1].get_text().replace('\n', '')
m7 = re.search(r'自治体による検査（～([0-9]+)月([0-9]+)日）：延([0-9,]+)人', text).group(3).replace(',', '')

# 更新日時取得
text = bs4(res.content, 'html.parser').select('.box_info_ttl span.txt_big')[0].get_text().replace('\n', '')
node = re.search(r'感染確認状況\(([0-9]+)月([0-9]+)日 現在\)', text).groups()
last_update = "{}\/{:02}\/{:02} {:02}:{:02}".format(dt.today().year, int(node[0]), int(node[1]), 21, 0)
file_name = dt.now().strftime("last_update_jokyo%Y%m%d-0.csv")
with open(file_name, 'w') as f:
    f.write(last_update)

# 切り出した値をもとにCSVファイルを生成する。
csv_file = dt.now().strftime('patients_%Y%m%d.csv')

if len(sys.argv) == 2 and re.match(r'[0-9]{8}', sys.argv[1]):
    csv_file = 'patients_{}.csv'.format(sys.argv[1])

with open(csv_file, 'w') as f:
    f.write("{},{},{},{},{},{},{}\n".format(m1, m2, m3, m4, m5, m6, m7))

