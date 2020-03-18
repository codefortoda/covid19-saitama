# Save csv data from opendata page to file
import urllib3
import re
from bs4 import BeautifulSoup
import datetime


# data_type: now supports "jokyo" or "kensa"
def get_opendata_from_url(data_type):
    # Get html data from portal page 
    http = urllib3.PoolManager()
    url = "https://opendata.pref.saitama.lg.jp/data/dataset/covid19-" + \
            data_type
    r = http.request('GET', url)
    soup = BeautifulSoup(r.data, 'html.parser')

    # Get yesterday as format '20200101'
    date = datetime.datetime.strftime(datetime.datetime.now() - \
            datetime.timedelta(days=1),"%Y%m%d")
    link = soup.find_all(href=re.compile((\
            "https://opendata.pref.saitama.lg.jp/data/dataset/.*/%s%s\.csv"\
            % (data_type, date))))

    # Save csv data
    for i, atag in enumerate(link):
        csv = http.request('GET', atag["href"])
        decoded_data = csv.data.decode('shift-jis')
        file_name = "%s%s-%s.csv" % (data_type, date, i)
        with open(file_name, 'w') as f:
            f.write(decoded_data)
            print("Saving "+ file_name)

    print(data_type + " done.")


get_opendata_from_url("jokyo")
get_opendata_from_url("kensa")
