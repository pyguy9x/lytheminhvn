'''
VNExpress crawler: only title of site
Coded by: Ly The Minh
All rights reserved (C) July-2021
'''
# Crawl library
import requests
from bs4 import BeautifulSoup
# sleep
import time
# Get rss database form file
rss_db = []
#! Require rss.txt has in current folder
with open("rss.txt","r") as file:
	for line in file:
		rss_db.append(line.strip())
# List of url to be crawl
base_url = [f"https://vnexpress.net/rss/{i}.rss" for i in rss_db]
# base_url = "https://vnexpress.net/rss/so-hoa.rss"
# Saving file
with open("vnexpress5.txt","w",encoding="utf-8") as file:
	for u in base_url:
		temp = u.split("/")[4]
		catagory= temp[0:len(temp)-4] #=> tim-moi-nhat

		r = requests.get(u)
		r_soup = BeautifulSoup(r.content,features="xml")
		title = r_soup.findAll('title')
		pub_date = r_soup.findAll('pubDate') # Publish date
		url = r_soup.findAll('link')
		# Remove header
		title.pop(0)
		url.pop(0)
		# print(len(pub_date))
		# print(len(title))
		# print(len(url))
		file.write(f'\nTotal news in {u}: {len(title)}\n')
		for i,v in enumerate(title):	
			# txt = f'{v.text} \nNgày đăng: {pub_date[i].text}\n{url[i].text}\n'
			# data = f'{v.text}-Ngày đăng: {pub_date[i].text}=>{url[i].text}\n'
			txt = v.text			
			if "Tin nhanh VnExpress" not in str(txt):
				print(f"{txt} _ [{catagory}] ")
				# data = v.text+f"({pub_date[i].text})=>{url[i].text}\n"
				# file.write(data)
				# file.write(f"{txt} _ [{catagory}]\n")
				file.write(f"{txt}\n")
		print(f'\nTotal news in {u}: {len(title)}')
		print("="*60)
		time.sleep(1) # Delay
print("All done VNexpress")