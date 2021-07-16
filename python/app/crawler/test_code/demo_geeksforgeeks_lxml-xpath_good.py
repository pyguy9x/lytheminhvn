# Python3 code implementing web scraping using lxml
  
import requests
  
# import only html class
from lxml import html 
  
# url to scrape data from
url = 'https://www.geeksforgeeks.org'
  
# path to particular element
path = '//*[contains(@id,"post")]/div/div[1]/a'
# --> Tìm các id có url chứa "post", vd: //*[@id="post-610588"]/div/div[1],//*[@id="post-610966"]/div/div[1]/a,...
  
# get response object
response = requests.get(url)
  
# get byte string
byte_data = response.content
  
# get filtered source code
source_code = html.fromstring(byte_data)
  
# jump to preferred html element
tree = source_code.xpath(path)
  
# print texts in first element in list
# print(tree[2].text_content())
for title in tree:
	print(title.text_content())
# print(dict(tree))