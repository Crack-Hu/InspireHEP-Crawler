import requests
import json
from bs4 import BeautifulSoup
import os, sys
import time, random

aim_dir = sys.argv[1]
collection_path = os.path.join(aim_dir, 'citation_collection.txt')

url_api = f'https://inspirehep.net/api/literature/'
dir_json = os.path.join(aim_dir, 'origin_json')
if not os.path.exists(dir_json):
    os.makedirs(dir_json)

def get_raw_json(inspire_id):
    url = url_api + inspire_id
    temp = requests.get(url, stream=True)
    return temp.text
    #  rawdate = json.loads(temp.text)

    with open(os.path.join(dir_json, f'{inspire_id}.json'), 'w') as f:
        f.write(temp.text)

with open(collection_path, 'r') as f:
    id_list = f.readlines()
    id_list = [[ii.strip() for ii in i.split(',')] for i in id_list]
    id_list.sort(key=lambda x: int(x[0][1:]))

length = len(id_list)

for i in id_list:
    file_path = os.path.join(dir_json, f'{i[0]}.json')
    if os.path.exists(file_path):
        continue
    
    print(f'now processing id:{i[0]}...', end='\r')
    print(f' '*40, end='\r')
    print('requesting', end = '\r')
    print(f' '*40, end='\r')
    temp = get_raw_json(i[1])
    with open(file_path, 'w') as f:
        f.write(temp)
    print(f'hanging on,{int(i[0]/length)}% finished', end='\r')
    print(f' '*40, end='\r')
    time.sleep(random.uniform(0.5,2))
#  metadata = rawdate['metadata']
#  title = metadata['title']
#  keywords = metadata['keywords']
#  abstracts = metadata['abstracts']
