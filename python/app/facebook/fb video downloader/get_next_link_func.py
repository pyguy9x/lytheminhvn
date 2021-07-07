from requests import session
import time
s = session()

def get_link(idPage):
	# idPage = 'tran.thanh.ne'
	access_token = 'your token'
	myList = []

	_api = s.get('https://graph.facebook.com/v3.3/' + str(idPage) + '?fields=videos{source,length}&access_token=' + access_token).json()

	if 'Some of the aliases you requested do not exist' in str(_api):
		print("Error: Trang không tồn tại!")
		return "Error: Trang không tồn tại!"
	if 'next' in str(_api):
		next_page = _api["videos"]["paging"]["next"] # this is first page!
		myList.append(next_page)
		_api = s.get(next_page).json() # turn to page 1
	else:
		next_page = ""
	if 'data' not in str(_api):
		print("Error: Không có video!")
		return "Error: Trang không tồn tại!"
	print("--- Start ---")
	count=0
	while True:
		print(".",end="")
		time.sleep(0.5)
		if 'next' in str(_api):
			next_page = _api["paging"]["next"]
			myList.append(next_page)
			count+=1
			_api = s.get(next_page).json()
		else:
			print("\n--END of page--")
			count+=1
			break
		pass
	print("Total page link: ",count)
	# print(myList)
	return myList

def get_video(vlink,vlength):
	myVid = []
	i=0
	while True:
		time.sleep(0.1)
		try:
			data = s.get(vlink).json()			
			if int(data['data'][i]['length']) <= int(vlength):
				d = data['data'][i]['source']
				myVid.append(d)
				print(data['data'][i]['id'])
				i+=1
			else:
				print("over size")
				break
		except IndexError:
			break
		except KeyError:
			break
	return myVid