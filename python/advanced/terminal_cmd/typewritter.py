import sys,time,os

speed = 0.01
message1 = "This tutorial shows you how you can add typewriter style animated text to your Python programs quickly and easily. \nThis is especially useful when you are creating dialogue screens for adventure RPG games. \nWorks in Linux and Windows\n"
message2 = "VnExpress hay Tin nhanh Việt Nam\nlà một trang báo điện tử tại Việt Nam được thành lập bởi tập đoàn FPT, ra mắt vào ngày 26 tháng 02 năm 2001 và được Bộ Văn hóa - Thông tin cấp giấy phép số 511/GP - BVHTT ngày 25 tháng 11 năm 2002, hiện tại do FPT Online quản lý."
def typewriter(message):
	for char in message:
		sys.stdout.write(char)
		sys.stdout.flush()

		if char != '\n':
			time.sleep(speed)
		else:
			time.sleep(1)
os.system("cls") 
os.system("color a")

typewriter(message1+message2)

# with open("index.html","r",encoding="utf-8") as file:
# 	for line in file:
# 		typewriter(line)


