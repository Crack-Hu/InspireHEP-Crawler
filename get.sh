#!/bin/sh

#  $1 for inspire_id 
#  $2 denote the directory path
#  $3 denote the final json result path

echo "Starting citation atricles id crawling, html would stored in ./${2}/origin_html"
python3 crawl_selenium.py $1 $2

echo "Analyzing the origin html, get all citation's inpirehep id, stroed in ./${2}/citation_collection.txt"
python3 bs.py $2

echo "Starting citations information crawling, json would stored in ./${2}/origin_json"
python3 get_rawdata.py $2

echo "Merging all the jsons"
python3 join.py $2 $3
