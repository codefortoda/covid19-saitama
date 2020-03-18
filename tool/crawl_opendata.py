# Save csv data from opendata page to file
import urllib3
import re
from bs4 import BeautifulSoup
import datetime

# Get html data from portal page 
http = urllib3.PoolManager()
url = "https://opendata.pref.saitama.lg.jp/data/dataset/covid19-jokyo"
r = http.request('GET', url)
soup = BeautifulSoup(r.data, 'html.parser')

# Get yesterday as format '20200101'
date = datetime.datetime.strftime(datetime.datetime.now() - datetime.timedelta(days=1),"%Y%m%d")
link = soup.find_all(href=re.compile(("https://opendata.pref.saitama.lg.jp/data/dataset/.*/jokyo%s\.csv" % date)))

# Save csv data
for i, atag in enumerate(link):
    csv = http.request('GET', atag["href"])
    decoded_data = csv.data.decode('shift-jis')
    file_name = "jyokyo%s-%s.csv" % (date, i)
    with open(file_name, 'w') as f:
        f.write(decoded_data)
        print("Saving "+ file_name)

print("Done.")
