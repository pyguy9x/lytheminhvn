from requests import session
import urllib.request
import json
s = session()

access_token = "your token"

# idPage = "anchoivungtau"
# idPage = 'j2team.community'
idPage = 'dichvutrangtrisinhnhatCindy'

page_num = 1
first_page = True
total_videos_num = 0

# video dai 60s
video_length = 60

big_data = s.get('https://graph.facebook.com/' + str(idPage) + '?fields=videos{source,length}&access_token=' + access_token).json()
if 'next' in big_data["videos"]["paging"]:
	next_page = big_data["videos"]["paging"]["next"]
else:
	next_page = ""

print("Downloading...Ctr+C to quit\n")
while True:
	if first_page == True:
		data = big_data["videos"]["data"]
		first_page = False		
	else:
		data = big_data["data"]
	print("Page ", page_num)
	# print(next_page)
	count=0
	for x in data:		
		if 'source' in x:
			video_url = x['source']
			# Tai video
			# urllib.request.urlretrieve(video_url, 'video/video_name'+ str(count)+'.mp4')
			# Tai video duoi 30 giay
			if int(x['length']) < video_length:
				video_name = video_url[-8:]
				# urllib.request.urlretrieve(video_url, 'video/video_name'+ str(video_name)+'.mp4')
				# print(video_url[-5:],count,end=" ")
				print(x['length']," second")
				count+=1
	print("Videos Downloaded: ",count,"/",len(data))
	total_videos_num += count

	try:
		if next_page == "":
			print("No more page")
			break

		big_data = s.get(next_page).json()
		if 'next' in big_data["paging"]:
			next_page = big_data["paging"]["next"]
			# print(next_page)
		else:
			# Last page
			big_data = s.get(next_page).json()
			print("\nThe last one")
			count = 0
			for x in big_data['data']:
				if 'source' in x and int(x['length']) < video_length:
					video_url = x['source']
					video_name = video_url[-8:]
					# print(video_url[-5:],"(",count,")",end=" ")
					print(x['length']," second")
					# urllib.request.urlretrieve(video_url, 'video/video_name'+ str(video_name)+'.mp4')
					count += 1
			total_videos_num += count
		print("\nEnd of page!")
		break
	except Exception as e:
		raise e
		break
	print("")
	page_num += 1	

print("\nAll done videos: ",total_videos_num)