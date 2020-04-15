#!/bin/sh

python3 crawl_shingatacoronavirus.py
python3 get_from_jokyo_pdf.py
python3 csv2json.py
sed -i '' s'/\\\\/\\/g' data.json
cp ../data/data.json ../data/data.json.bak
cp data.json ../data/data.json
