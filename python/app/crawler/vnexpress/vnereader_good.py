'''
VNExpress crawler: show the data
Coded by: Ly The Minh
All rights reserved (C) July-2021
Comment: reference vnepress_speaker_good.py
'''
import sys,time,os
speed = 0.000001

def typewriter(message):
	for char in message:
		sys.stdout.write(char)
		sys.stdout.flush()

		if char == '\n':
			time.sleep(0.00001)
		else:
			time.sleep(speed)

def color_text(text,m=1):
	# m: mode
	if m == 1: # Blue
		return f"\033[44;1m\033[97m{text}\033[0m"
	elif m == 2: # Violet
		return f"\033[45;1m\033[97m{text}\033[0m"
	elif m == 3: # cyan
		return f"\033[46;1m\033[97m{text}\033[0m"
	elif m == 4: # gray
		return f"\033[47;1m\033[97m{text}\033[0m"
	elif m ==5: #black
		return f"\033[31;1m{text}\033[0m"
	else: # blue
		return f"\033[41;1m\033[97m{text}\033[0m"

# os.system("cls") 

typewriter("== 10 TIN TỨC " + color_text("MỚI NHẤT",m=5) +" 16-07-2021==")
data = []

print("\nNhập từ khóa quan tâm (Covid-19): ")
keyword = str(input("=> ") or "Covid-19").lower()
print("-"*30)

with open("vnexpress5.txt","r",encoding="utf-8") as file:
	for line in file:
		if keyword.lower() in str(line).lower():
			idx = line.lower().index(keyword)
			origin = line[idx:idx+len(keyword)]
			#hl: high-light			
			hl = line.replace("Covid" or "covid",color_text("COVID",5))
			hl = hl.replace(origin,color_text(origin))
			data.append(hl.strip())
cout = 0
# data = list(set(data)) # remove dupicated item, => error
data.pop(0)
for i,v in enumerate(data):
	cout +=1
	typewriter("[+] "+v.strip()+"\n")
	if cout == 10:
		break
print(color_text("Finished.",m=2))
