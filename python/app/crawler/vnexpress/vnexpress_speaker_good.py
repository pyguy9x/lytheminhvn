'''
VNExpress reader and speaker
Coded by: Ly The Minh
All rights reserved (C) July-2021
'''
import sys,time,os
# os: để chạy lệnh trên terminal, cụ thể là cls
# TTS: Text to speech
from gtts import gTTS
import playsound
# To make random name
import random
import string
# Len of code: UGRHNF => 6
N = 6
# Speed for typer
speed = 0.000001
# Typer writing
def typewriter(message):
	for char in message:
		sys.stdout.write(char)
		sys.stdout.flush()
		if char == '\n':
			time.sleep(0.00001)
		else:
			time.sleep(speed)
# Color in terminal. On windows, run Cmder.exe
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
# Speak
def speak_out(text):
	# Step 1: Get the message
	# Step 2: Turn into audio file
	# Step 3: Play audio file
	# Random name string, get rid of conflict
	name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
	output = gTTS(text,lang="vi", slow=False)
	# ! Require: Make "\wav" folder first
	output.save(f"wav\\output.wav")
	# Speed up audio
	# Change speed at : atempo=1.5
	# quiet: show nothing ~silent
	# -y: overwrite file
	ffmpeg = f'@echo OFF & ffmpeg.exe -loglevel quiet -i wav\\output.wav -filter:a "atempo=1.5" wav\\{name}.wav -y & exit /b'
	# ! Require: ffpmeg.exe has in current folder, or add ffmpeg into PATH
	# Run the command
	os.system(ffmpeg)
	# Speak
	playsound.playsound(f'wav\\{name}.wav', True)
	# Other way:
	# ff = ffmpy.FFmpeg(inputs={"output.wav": None}, outputs={"o.wav -y": ["-filter:a", "atempo=1.3"]})
	# ff.run()
	# Must delete this file, if not will be raise an error!	
	os.remove("wav\\output.wav")

# -----  MAIN -----
# os.system("cls") 
typewriter("== 10 TIN TỨC " + color_text("MỚI NHẤT",m=5) +" 16-07-2021==")
data = [] # news
data_origin = [] #only title, for speaking

print("\nNhập từ khóa quan tâm (Covid-19): ")
keyword = str(input("=> ") or "Covid-19").lower()
print("-"*30)
# vnexpress5.txt => change it
with open("vnexpress5.txt","r",encoding="utf-8") as file:
	for line in file:		
		if keyword.lower() in str(line).lower():
			# Get the position of keyword in string
			idx = line.lower().index(keyword)
			origin = line[idx:idx+len(keyword)]
			# hl: high-light
			# Decor them
			hl = line.replace("Covid" or "covid",color_text("COVID",5))
			hl = hl.replace(origin,color_text(origin))
			# Different data
			data.append(hl.strip()) # for showing with formatting
			data_origin.append(line.strip()) # for speaking
# ----- SHOW DATA -----
cout = 0
# Don't
# data = list(set(data)) # remove duplicated item
# data_origin = list(set(data_origin)) # remove duplicated item
# this makes it speak wrong line!
try:
	data.pop(0)
	data_origin.pop(0)
except IndexError:
	print(color_text("Từ khóa ko hợp lệ!",m=2))
	exit()

for i,v in enumerate(data_origin):
	cout +=1
	if "rss" not in v: # Title only
		typewriter("[+] "+data[i].strip()+"\n")
		speak_out(v.strip())
	if cout == 10: # Get 10 news first
		break
print(color_text("Finished.",m=2))
speak_out("Hết bản tin")