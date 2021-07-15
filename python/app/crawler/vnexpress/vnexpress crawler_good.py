import requests
from bs4 import BeautifulSoup
import time
# Get rss database
rss_db = []
with open("rss.txt","r") as file:
	for line in file:
		rss_db.append(line.strip())
# print(rss_db)
# exit()
base_url = [f"https://vnexpress.net/rss/{i}.rss" for i in rss_db]
# base_url = "https://vnexpress.net/rss/so-hoa.rss"
for u in base_url:
	r = requests.get(u)
	r_soup = BeautifulSoup(r.content,features="xml")
	title = r_soup.findAll('title')
	pub_date = r_soup.findAll('pubDate')
	# pub_date = r_soup.find_all(["pubDate", "pubDate"])
	url = r_soup.findAll('link')
	# Loai bo header
	title.pop(0)
	url.pop(0)
	# print(len(pub_date))
	# print(len(title))
	# print(len(url))
	with open("vnexpress.txt","w",encoding="utf-8") as file:
		for i,v in enumerate(title):
			try:	
				# txt = f'{v.text} \nNgày đăng: {pub_date[i].text}\n{url[i].text}\n'
				data = f'{v.text}-Ngày đăng: {pub_date[i].text}=>{url[i].text}\n'
				txt = v.text
				print(txt)
				file.write(data)
			except IndexError:
				break
		print(f'\nTotal news in {u}: {len(title)}')
		file.write(f'Total news in {u}: {len(title)}')
		print("="*60)
	time.sleep(1)
print("All done VNexpress")