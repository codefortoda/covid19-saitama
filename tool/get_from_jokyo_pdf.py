# pip install tika
# 初回のみtika.jarのダウンロードに時間がかかります
from tika import parser
import re

# PDF落としとく分は後で考えますが、urllib3使えばすぐかもしれません
# 最初はwget http://www.pref.saitama.lg.jp/a0701/covid19/documents/itiran0403.pdf でも実行してください
file_data = parser.from_file("itiran0403.pdf")
lines = file_data['content'].split('\n')
with open("list0403.csv", "w+") as f:
    f.write("No.,判明日,年代,性別,居住地,入院中\n")
    for l in lines:
        if len(l) > 0 and l[0].isdecimal():
            data = l.split()
            pos = 2

            # 8 8 リンク先概要2 みたいなデータの場合1列追加
            if data[pos-1].isdecimal() and not(data[pos][0].isdecimal()):
                pos += 1

            match = re.match("(.*)月(.*)日", data[pos])
            date_text = '2020/'+ match.group(1) + '/' + match.group(2)
            f.write("%s,%s,%s,%s,%s, \n" % (data[0], date_text, data[pos+1], \
                    data[pos+2], data[pos+3]))

date = "20200403"
file_name = file_name = "%s%s-%s.csv" % ("jokyo", date, 0)
with open("last_update_" + file_name, 'w') as f:
    f.write("2020/04/03 20:00")
    print("Saving "+ "last_update_" + file_name)
