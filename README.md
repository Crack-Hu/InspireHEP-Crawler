# InspireHEP-Crawler

### python module needed
- bs4
- lxml
- selenium
    - a driver is needed. For google-chrome, check its version, download related driver in ```http://chromedriver.storage.googleapis.com/index.html```, and put it into ```/usr/bin```
- requests

### get.sh
- Usage : ```bash get.sh <inspirehep_id> <temporary_directory> <target_json>```
    - ```get.sh``` gives the json file as a result, and a handy json search engine is needed, here I recommand meilisearch (a github repository ```/meilisearch/meilisearch```)

##### ```get.sh``` just give an easy way to use. Here is the detail of each module:
- crawl_selenium.py
    - Usage : ```python3 crawl_selenium.py <inspirehep_id> <temporary_directory>```
    - Open the broswer (headless mod) and collect the citations of article with ```<inspirehep_id>```.
    - The html would stored in ```./<temporary_directory>/origin_html```.

- bs.py
    - Usage : ```python3 bs.py <temporary_directory>```
    - Analyze the htmls to get the inspire_id of citations.
    - The ```<rank:inspire_id>``` information would stored in ```./<temporary_directory>/citations_collection.txt```.

- get_rawdata.py
    - Usage : ```python3 get_rawdata.py <temporary_directory>```
    - Gives the final json of all citations, with the whole information, but in fragmented files.

- join_rawdate.py
    - Usage : ```python3 join_rawdata.py <temporary_directory> <target_json>```
    - Gives the final json of all citations, with ```titles```, ```key_words```, ```abstracts```    

### two script to give the collections of given json
- intersection.py
    - Usage : ```python3 intersection.py 1.json 2.json ... re.json```

- union.py
    - Usage : ```python3 union.py 1.json 2.json ... re.json```

### usage for meilisearch
- a quick start guide see ```https://docs.meilisearch.com/learn/getting_started/quick_start.html```
- run meilisearch in the current directory
- run ```curl \
  -X POST 'http://localhost:7700/indexes/db_name/documents' \
  -H 'Content-Type: application/json' \
  --data-binary @temp_json.json``` where db_name should be replaced by the name you want, and temp_json.json is the json file you want to deal with.
