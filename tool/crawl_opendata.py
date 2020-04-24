# Save csv data from opendata page to file
# Usage: 
#    $ python3 crawl_opendata.py
#    $ python3 crawl_opendata.py 20200330

import urllib3
import re
import sys
from bs4 import BeautifulSoup
import datetime


# data_type: now supports "jokyo" or "kensa"
def get_opendata_from_url(data_type, date, pattern_text):
    # Get html data from portal page 
    url_header = "https://opendata.pref.saitama.lg.jp/data/dataset/"
    
    http = urllib3.PoolManager()
    url = url_header + "covid19-" + data_type
    r = http.request('GET', url)
    soup = BeautifulSoup(r.data, 'html.parser')

    if date == '':
        # Get yesterday as format '20200101'
        date = datetime.datetime.strftime(datetime.datetime.now() - \
            datetime.timedelta(days=1),"%Y%m%d")
    links = soup.find_all( href=re.compile(("%s.*/%s%s\.csv"\
            % (url_header, data_type, date))))

    # Save csv data
    for i, atag in enumerate(links):
        file_name = "%s%s-%s.csv" % (data_type, datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d"), i)
 
        # get recent update time of the file
        mat = re.match("%s.*/resource/(.*)/download/%s%s\.csv"\
            % (url_header, data_type, date), atag["href"])
        id = mat.group(1)
        #print("id ", id)
        recent_update_link = soup.find(href=re.compile(\
                "/data/dataset/covid19-%s/resource/%s" % (data_type, id)))
        #print(recent_update_link["title"])
        mat = re.match(pattern_text, recent_update_link["title"])
        recent_update = mat.group(1)
        #print(recent_update)
        with open("last_update_" + file_name, 'w') as f:
            f.write(recent_update)
            print("Saving "+ "last_update_" + file_name)

        csv = http.request('GET', atag["href"])
        decoded_data = csv.data.decode('shift-jis')
        with open(file_name, 'w') as f:
            f.write(decoded_data)
            print("Saving "+ file_name)

    print(data_type + " done.")


if len(sys.argv) == 2:
    date = sys.argv[1]
else:
    date = ''

# get_opendata_from_url("jokyo", date,  "埼玉県内の新型コロナウイルス感染症の発生状況（(.*)）")
get_opendata_from_url("kensa", date, "埼玉県が実施した新型コロナウイルス疑い例検査数（延べ人数）（(.*)）")
