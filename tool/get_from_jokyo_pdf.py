# usage
# Java8以降が必要
# $ python get_from_jokyo_pdf.py http://www.pref.saitama.lg.jp/a0701/covid19/documents/yousei04082000.pdf
# 前日のデータを取得
# $ python get_from_jokyo_pdf.py http://www.pref.saitama.lg.jp/a0701/covid19/documents/yousei04071600.pdf 20200407
# 2020年3月31日のデータを取得
# 初回のみtika.jarのダウンロードに時間がかかります
import re
import sys
import urllib3
import datetime
import requests
from tika import parser
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# 一旦成功前提でTrue返しときますが、例外発生時にはFalse返すように
# してもいいかもしれません
def get_pdf_file(monthday: str, url: str) -> bool:
    if url == '':
        url_jokyo = "http://www.pref.saitama.lg.jp/a0701/covid19/jokyo.html"
        r = requests.get(url_jokyo)
        soup = BeautifulSoup(r.content, "html.parser")
        tag = soup.find("a", text=re.compile("^陽性確認者一覧.+?PDF"))
        url = urljoin(url_jokyo, tag.get("href"))

    file_name = "itiran%s.pdf" % monthday
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    with open(file_name, "wb") as f:
        f.write(r.data)
    return True

def main(date: str, url: str) -> None:

    if date == '':
        date = datetime.datetime.strftime(datetime.datetime.now() - \
            datetime.timedelta(days=0),"%Y%m%d")
    monthday = date[4:]

    # PDFを保存します
    get_pdf_file(monthday, url)
    file_data = parser.from_file("itiran%s.pdf" % monthday)
    lines = file_data['content'].split('\n')
    with open("list%s.csv" % date, "w+") as f:
        f.write("No.,判明日,年代,性別,居住地,入院中\n")
        for l in lines:
            if len(l) > 0 and l[0].isdecimal():
                data = l.split()
                pos = 2

                # 8 8 リンク先概要2 みたいなデータの場合1列追加
                if data[pos-1].isdecimal() and not(data[pos][0].isdecimal()):
                    pos += 1

                if data[pos] == "調査中":
                    date_text = "調査中"
                else:
                    match = re.match("(.*)月(.*)日", data[pos])
                    date_text = '2020/'+ match.group(1) + '/' + match.group(2)

                if re.match("(.*)[市町村]", data[pos+1]):
                    city = data[pos+1]
                    gender = ''
                    age = ''
                elif re.match("(.*)[性]", data[pos+1]):
                    # 年齢が「10歳未満」の場合に「”10歳未満”+性別」となるため、年齢・性別を分割
                    age = data[pos+1][-2:]
                    gender = data[pos+1][:-2]
                    city = data[pos+2]
                else:
                    gender = data[pos+1]
                    age = data[pos+2]
                    if len(data) >= pos+4:
                        city = data[pos+3]
                    else:
                        city = ''
                f.write("%s,%s,%s,%s,%s, \n" % (data[0], date_text, gender, \
                    age, city))
        print("Saving list%s.csv" % date )

date = ""
url = ""
if len(sys.argv) > 1:
    url = sys.argv[1]
    if len(sys.argv) == 3:
        date = sys.argv[2]
main(date, url)
