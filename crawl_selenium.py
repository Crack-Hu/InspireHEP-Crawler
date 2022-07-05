from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time, random
import sys, os


inspirehep_id = sys.argv[1]
aim_dir = sys.argv[2]

origin_dir = os.path.join(aim_dir, 'origin_html')
if not os.path.exists(aim_dir):
    os.makedirs(aim_dir)
    if not os.path.exists(origin_dir):
        os.makedirs(origin_dir)


page_length = 10
pending_url = f"https://inspirehep.net/literature?sort=mostrecent&size=250&page=1&q=refersto%3Arecid%3A{inspirehep_id}"


ch_options = webdriver.ChromeOptions()
#  ch_options.add_argument("--headless")
#  ch_options.add_argument('--no-sandbox')
#  ch_options.add_argument('--disable-gpu')
#  ch_options.add_argument('--disable-dev-shm-usage')
wd = webdriver.Chrome(options=ch_options)

for page in range(1, page_length + 1):
    print(f'processing page {page}')
    pending_url_page = pending_url.replace('page=1', f'page={page}')
    wd.get(pending_url_page)
    print('waiting for broswer loading')
    WebDriverWait(wd, 60).until(EC.visibility_of_element_located((By.CLASS_NAME, 'mv2')))
    print('html saving')
    with open(os.path.join(origin_dir, f'html{page}.html'), 'w') as f:
        f.write(wd.page_source)
    print('hanging on')
    time.sleep(random.uniform(0.5,3))



