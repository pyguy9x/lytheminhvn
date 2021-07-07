from requests import session
import urllib.request
import json
# make unique video name
import string
import random
import time
s = session()

# make random name for video name
def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

access_token = "your token"

# idPage = "anchoivungtau"
# idPage = 'j2team.community'
def Get_Video(page_id='dichvutrangtrisinhnhatCindy', video_len=30):	
	# idPage = 'dichvutrangtrisinhnhatCindy'
	idPage = page_id

	page_num = 1
	first_page = True
	total_videos_num = 0
	allvideo = {}

	# video dai 60s
	# video_length = 60
	video_length = int(video_len)

	big_data = s.get('https://graph.facebook.com/v3.3/' + str(idPage) + '?fields=videos{source,length}&access_token=' + access_token).json()

	if 'Some of the aliases you requested do not exist' in str(big_data):
		return "Error: Trang không tồn tại!"
	if 'next' in str(big_data):
		next_page = big_data["videos"]["paging"]["next"]
	else:
		next_page = ""
	if 'data' not in str(big_data):
		return "Error: Không có video!"

	print("Downloading...Ctr+C to quit\n")
	while True:
		if first_page == True:
			data = big_data["videos"]["data"]
			next_page = big_data["videos"]["paging"]["next"]
			first_page = False		
		else:
			data = big_data["data"]
			if 'next' in str(big_data["paging"]):
				next_page = big_data["paging"]["next"]
			else:
				break
		print("\nPage ", page_num)
		# print(next_page)
		count=0
		for x in data:		
			if 'source' in str(x) and int(x['length']) < video_length:
				video_url = x['source']
				video_dodai = x['length']
				# Tai video
				# urllib.request.urlretrieve(video_url, 'video/video_name'+ str(count)+'.mp4')		
				video_name = video_url[-8:]
				# ten ngau nhien
				vdName = get_random_string(12)
				allvideo[vdName] = {"video":video_url,"length":video_dodai}
				count+=1
		print("Videos Downloaded: ",count,"/",len(data))
		total_videos_num += count
		print()
		try:
			big_data = s.get(next_page).json()
			if 'next' in str(big_data["paging"]):
				next_page = big_data["paging"]["next"]
				data = big_data["data"]
				count=0
				for x in data:		
					if 'source' in str(x) and int(x['length']) < video_length:
						video_url = x['source']
						video_dodai = x['length']
						# Tai video
						# urllib.request.urlretrieve(video_url, 'video/video_name'+ str(count)+'.mp4')		
						# ten ngau nhien
						vdName = get_random_string(12)
						allvideo[vdName] = {"video":video_url,"length":video_dodai}
						count+=1
				print("next ",next_page)
				big_data = s.get(next_page).json()
				if 'next' in str(big_data['paging']):
					next_page = big_data["paging"]["next"]
					page_num += 1
				else:
					print("--END--")			
					break
		except Exception as e:
			raise e
			print(e)
			break
	print("")		
	time.sleep(1)
	return allvideo
# Tra ve dang the nay
# allvideo = {
# idvideo1 {'video': 'linkvideo1','length': 'length_video1'}
# idvideo2 {'video': 'linkvideo2','length': 'length_video2'}
# idvideo3 {'video': 'linkvideo3','length': 'length_video3'}
# idvideo4 {'video': 'linkvideo4','length': 'length_video4'}
# }