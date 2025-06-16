from bs4 import BeautifulSoup
import os, sys

aim_dir = sys.argv[1]

html_path = os.path.join(aim_dir, 'origin_html')

collection_path = os.path.join(aim_dir, 'citation_collection.txt')

def info(box):
    box_id = box.find('div', attrs= {'data-test-id':'literature-result-rank'})
    box_id = box_id.text
    box_link = box.find('a', attrs = {'data-test-id':"literature-result-title-link"})
    box_link = box_link['href']
    box_link = box_link.split('/')[2]
    return (box_id, box_link)

ff = open(collection_path, 'w')

html_list = os.listdir(html_path)
html_list.sort()
total_len = len(html_list)
count = 1

for html_file in html_list:
    with open(os.path.join(html_path, html_file), 'r') as f:
        bs = BeautifulSoup(f.read(), 'lxml')

    re_temp = bs.find_all(name = 'div', attrs = {'class':'mv2'})
    for box in re_temp:
        ff.write(','.join(info(box)) + '\n')
    print(f'\rprocessing {(count*100/total_len)}%', end = '', flush = True)
    count += 1
print('')

ff.close()
