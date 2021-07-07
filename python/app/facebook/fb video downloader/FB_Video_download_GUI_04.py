## Chay on dinh ! K chinh sua gi them !
from tkinter import *
from tkinter import scrolledtext,messagebox
import tkinter.scrolledtext as scrolledtext
import get_next_link_func as MyFunc
import time
import threading

global dt
dt=1
# dùng thread cho đỡ lag
def get_button():
	t1 = threading.Thread(target=test).start()

def down_button():
	t2 = threading.Thread(target=dwn_button).start()

def dwn_button():
	dem=0
	global data
	global dt
	dodai = duration_ui.get()
	idPage = str(ID_page_ui.get())
	if idPage == "" or dodai =="" or dodai.isnumeric()==False:
		messagebox.showwarning('Lỗi','Chưa nhập đúng')
	else:
		dwn_btn['text'] = '[+] Đang lấy video...'		
		get_btn['state'] ='disable'  # enabled
		dwn_btn['state'] ='disable'  # enabled
		for v in data:				
			# result_ui.insert(END,v) # insert text into textarea
			# result_ui.insert(END,"\n\n") # insert text into textarea
			video = MyFunc.get_video(v,int(dodai))
			for i in video:
				result_ui.insert(END,i) # insert text into textarea
				result_ui.insert(END,"\n\n") # insert text into textarea
				# Tai video
				# urllib.request.urlretrieve(video_url, 'video/video_name'+ str(count)+'.mp4')
				dem+=1
		# Quet xong
		get_btn['state'] ='normal'  # enabled
		get_btn['text'] = "[1] Lấy thông tin"			
		ID_page_ui['state'] ='normal'  # enabled			
		result_ui.insert(END,'\n[+] Total videos: '+str(dem)+"\n----------\n") # insert text into textarea
		# result_ui['state'] = 'disable'		
		dwn_btn['text'] = "[2] Lấy video"
		dwn_btn['state'] = 'disable'
		messagebox.showinfo('Result','Download done! Total videos: '+str(dem))
		
	i=0
	data=[]
	pass
window = Tk()

def test():		
	idPage = str(ID_page_ui.get())
	dodai = duration_ui.get()
	global data
	if idPage == "" or dodai =="" or dodai.isnumeric()==False:
		messagebox.showwarning('Lỗi','Chưa nhập đúng')
	else:
		get_btn['text'] = "[1] Đang lấy dữ liệu...Vui lòng đợi"		
		result_ui.insert(END,"[+] Vui lòng đợi...\n")
		
		get_btn['state'] ='disable' 
		ID_page_ui['state'] ='disable' 
		# result_ui['state'] = 'normal'		
		data = MyFunc.get_link(idPage)		
		if 'Error' not in data:
			get_btn['text'] = "[OK] Xong"			
			get_btn['state'] = "disable"			
			result_ui.insert(END,"[+] Đã lấy xong. Danh sách video từ " + idPage.upper() + "\n")
			dwn_btn['state'] = 'normal'
			dwn_btn['text'] = '[2] Lấy video'
			result_ui.insert(END,"[~] Số trang " + str(len(data)) + ".\n")
		else:
			messagebox.showwarning('Lỗi',str(data))
			get_btn['state'] ='normal'  # enabled			
			ID_page_ui['state'] ='normal'  # enabled			
			result_ui['state'] = 'disable'
			get_btn['text'] = "[1] Lấy thông tin"			
	# print(data)
			

window.wm_title("FB Video Downloader")
window.geometry('600x500+300+50')
# kich thuoc la 600x500
# vi tri xuat hien la x=300 va y=50
# ----------------- giao dien 2
# creat frame
my_lbl_frame = LabelFrame(window,text=" Nhập ID Page và thời lượng video (tính = giây)")
my_lbl_frame.pack(pady=20,fill="both",padx=20)

# creat textbox
ID_page_ui = Entry(my_lbl_frame,font=("Segoe UI",12))
ID_page_ui.pack(padx=20, pady=10,fill=X)
# ID_page_ui.insert(0,'dichvutrangtrisinhnhatCindy')
# ID_page_ui.insert(0,'tran.thanh.ne')
# ID_page_ui.insert(0,'kimquykiwi')
ID_page_ui.insert(0,'huongtram.official')

duration_ui = Entry(my_lbl_frame,font=("Segoe UI",12))
duration_ui.pack(padx=20, pady=10,fill=X)
duration_ui.insert(0,'50')

# creat textbox frame
myframe = Frame(window)
myframe.pack(pady=20,padx=20,fill='both')

# creat vertical scrollbar
text_scroll = Scrollbar(myframe)
text_scroll.pack(side=RIGHT, fill=Y)

# creat horizontal scrollbar
hor_scroll = Scrollbar(myframe, orient='horizontal')
hor_scroll.pack(side=BOTTOM, fill=X)

# creat textarea
result_ui = Text(myframe, yscrollcommand=text_scroll.set, wrap=CHAR, xscrollcommand=hor_scroll.set,bg="ivory3",fg="blue")
result_ui.pack(fill='both', expand=True)

# configure frame
text_scroll.config(command=result_ui.yview)
hor_scroll.config(command=result_ui.xview)

# button
btn_frame = Frame(window)
btn_frame.pack(pady=10)

get_btn = Button(my_lbl_frame, command=get_button,text="[1] Lấy thông tin",bg="light green",font=("Helvatica",15))
get_btn.pack(fill=X,padx=20,pady=10,side=LEFT)

# dwn_btn = Button(my_lbl_frame, command=down_button,text="[2] Lấy video",bg="tomato",font=("Helvatica",15))
dwn_btn = Button(my_lbl_frame, command=down_button,text="[2] Lấy video",bg="tomato",font=("Helvatica",15))
dwn_btn.pack(fill=X,padx=20,pady=10,side=RIGHT)

# result_ui['state'] = 'disable'
# dwn_btn['state'] = 'disable'
window.mainloop()
