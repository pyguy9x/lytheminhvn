import concurrent.futures
import time
import requests
from lxml import html
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://news.ycombinator.com/"
STORY_LINKS = [f'{BASE_URL}news?p={i}' for i in range(1,11)]

print(len(STORY_LINKS))
print("Begin")
# path = '//*[contains(@id,"normalthread")]/div/div[1]'
path = '//*[contains(@id,"")]/td[3]/a'
count = 0
for i in STORY_LINKS:
    # get response object
    response = requests.get(i)
      
    # get byte string
    byte_data = response.content
      
    # get filtered source code
    source_code = html.fromstring(byte_data)
      
    # jump to preferred html element
    tree = source_code.xpath(path)
      
    # print texts
    for title in tree:
        print(title.text_content())
    count+=1
    time.sleep(0.25)
    print("--------next page ",count)