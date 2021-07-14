import requests
import time
from bs4 import BeautifulSoup
# -------------------Craw all------------------------------
# start_urls = [f'https://ghiencongnghe.info/dien-thoai/android/page/{i}' for i in range(1,16)]
# start_urls = [f'https://ghiencongnghe.info/may-tinh/windows/page/{i}' for i in range(1,16)]
start_urls = [f'https://ghiencongnghe.info/may-tinh/macos/page/{i}' for i in range(1,16)]
# start_urls = [f'https://ghiencongnghe.info/dien-thoai/ios/page/{i}' for i in range(1,20)]
formatted_links = []
print("Getting link...")
page = 0
for i in start_urls:
	r = requests.get(i)
	soup = BeautifulSoup(r.text, 'html.parser')
	if "Lỗi 404" in str(soup):
		break
	links = soup.findAll('h3', class_='post-title')
	for link in links:
		tieude = list(link.children)[0].get_text()
		# print(tieude)
		url = link.find('a')['href']
		data = {
			# 'id': link['id'],
			'title': tieude,
			"url": url
			# "rank": int(links[0].td.span.text.replace('.', ''))
		}
		formatted_links.append(data)
	page += 1
	print(page,end=",")
	time.sleep(0.5)	
print("\nGet done, page: ",page)
print()
for i in range(len(formatted_links)):
	print(dict(formatted_links[i])['title'])
	print(dict(formatted_links[i])['url'])
	print()
print("Done: ",len(formatted_links))



