import requests
from bs4 import BeautifulSoup

base_url = "http://mp3.zing.vn"

r = requests.get(base_url)
r_soup = BeautifulSoup(r.text, "html.parser")
song_name = r_soup.findAll('h3',{'class':'song-name ellipsis'})
singer_list = r_soup.findAll('h4',{'class':'title-sd-item txt-info'})
# singer_list = r_soup.findAll('title').title
print("Top 10 Hits")
# print(singer_list)
for i,v in enumerate(song_name):
	if "Butter" not in v.text:
		print(i+1,v.text.strip(),'-',singer_list[i].text)
	else:
		break


