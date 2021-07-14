import concurrent.futures
import time
import string
import random
import requests
from lxml import html
import requests
from bs4 import BeautifulSoup

end_page = 3
code_len = 6

POST_LINKS = [f'https://c.mi.com/forum-127-{i}.html' for i in range(1,end_page)]

print(f"Ready to crawl {len(POST_LINKS)} page.")

f = open("cmicom.txt", "w", encoding="utf-8")

t0 = time.time()
# path = '//*[contains(@id,"normalthread_")]/div/div[1]'
path_tieude = '//*[contains(@id,"normalthread_")]/div/div[1]/div[2]/h4/a'
# path_nhom = '//*[contains(@id,"normalthread_")]/div/div[1]/div[2]/h4/em'
path_url = '//*[contains(@id,"normalthread_")]/div/div[1]/div[2]/h4/a/@href'

# //*[@id="normalthread_3758469"]/div/div[1]
count = 0
for i in POST_LINKS:
    # get response object
    response = requests.get(i)
      
    # get byte string
    byte_data = response.content
      
    # get filtered source code
    source_code = html.fromstring(byte_data)
      
    # jump to preferred html element
    tree0 = source_code.xpath(path_tieude)
    tree1 = source_code.xpath(path_url)
  
    # print texts
    try:
        random_code_db = [''.join(random.choices(string.ascii_uppercase + string.digits, k=code_len)) for k in range(len(tree0))]
        random_code_db_unique = list(set(random_code_db))
        print(random_code_db_unique)
        random_code = iter(random_code_db_unique)
        for url in tree1:
            for title in tree0:
                print(title.text_content())
            # print(next(random_code),title.text_content())
                data = f"{next(random_code)},td:{title.text_content()},url:{url}\n"
            # f.writelines(next(random_code),title.text_content())
                f.writelines(data)
        # exit()
        count+=1    
        print("--------next page ",count)
        time.sleep(0.25)
    except StopIteration:
        break
f.close()
t1 = time.time()
print(f"{t1-t0} seconds to crawl {len(POST_LINKS)} threads in forum.")