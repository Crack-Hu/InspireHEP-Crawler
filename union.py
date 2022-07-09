import json
import sys, os

file_list = sys.argv[1:-1]
re_json_file = sys.argv[-1]

json_list = []

for f in file_list:
    with open(f, 'r') as f_temp:
        json_list.append(json.loads(f_temp.read()))

re_json = json_list[0]
json_list = json_list[1:]

for json_temp in json_list:
    link_temp_list = [i['link'] for i in json_temp]
    re_json = [i for i in re_json if i['link'] not in link_temp_list]
    re_json.extend(json_temp)

with open(re_json_file, 'w') as f:
    f.write(json.dumps(re_json))
