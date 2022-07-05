import json
import os
import sys

aim_path = sys.argv[1]
origin_path = os.path.join(aim_path, 'origin_json')
if not os.path.exists(origin_path):
    os.makedirs(origin_path)
json_re_path = sys.argv[2]

file_list = os.listdir(origin_path)
file_list.sort()

re = []
count = 1

for i in file_list:
    with open(os.path.join(origin_path, i), 'r') as f_origin:
        raw_data = json.loads(f_origin.read())
        
        temp = {}
        metadata = raw_data['metadata']
        try:
            tempp = [i['title'].lower() for i in metadata['titles']]
            temp['titles'] = '\\'.join(tempp)
        except KeyError:
            temp['titles'] = None
        try:
            tempp = [i['value'].lower() for i in metadata['keywords']]
            temp['keywords'] = '\\'.join(tempp)
        except KeyError:
            temp['keywords'] = None
        try:
            temp['abstracts'] = [i['value'].lower() for i in metadata['abstracts']]
        except KeyError:
            temp['abstracts'] = None
        temp['id'] = count
        count += 1
        temp['link'] = f'https://inspirehep.net/literature/'+raw_data['id']
    re.append(temp)

with open(json_re_path, 'w') as f:
    f.write(json.dumps(re))
