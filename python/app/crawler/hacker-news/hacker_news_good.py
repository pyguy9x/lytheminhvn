import requests
import time
from bs4 import BeautifulSoup

# -----------------Craw one link-----------------
# r = requests.get('https://news.ycombinator.com')
# # Next: https://news.ycombinator.com/news?p=3 to 25
# soup = BeautifulSoup(r.text, 'html.parser')
# links = soup.findAll('tr', class_='athing')

# formatted_links = []

# for link in links:
# 	data = {
# 		'id': link['id'],
# 		'title': link.find_all('td')[2].a.text,
# 		"url": link.find_all('td')[2].a['href'],
# 		"rank": int(links[0].td.span.text.replace('.', ''))
# 	}
# 	formatted_links.append(data)

# for i in range(len(formatted_links)):
# 	print(dict(formatted_links[i])['title'])
#--------------------------------------
# -------------------Craw all------------------------------
start_urls = [f'https://news.ycombinator.com/news?p={i}' for i in range(1,6)]
formatted_links = []
print("Crawling...")

for i in start_urls:
	r = requests.get(i)
	# Next: https://news.ycombinator.com/news?p=3 to 25
	soup = BeautifulSoup(r.text, 'html.parser')
	links = soup.findAll('tr', class_='athing')
	for link in links:
		data = {
			# 'id': link['id'],
			'title': link.find_all('td')[2].a.text,
			"url": link.find_all('td')[2].a['href']
			# "rank": int(links[0].td.span.text.replace('.', ''))
		}
		formatted_links.append(data)
	time.sleep(0.5)

for i in range(len(formatted_links)):
	print(dict(formatted_links[i])['title'])
print("Done")



