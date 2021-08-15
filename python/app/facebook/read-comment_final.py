import requests
import json
import datetime
# lam viec voi excel
from xlwt import Workbook

# Ngay hom nay
time_now = datetime.datetime.now()
filename = time_now.strftime("%f")  # like 057718
# Data
log = []  # ghi lại nhật ký
sender = []  # tên người bình luận và phản hồi
total = 0  # tổng số cmt và reply
# id_view = 100003880469096 # juno okyo
# id_view = 179034362668856 # j2team
# id_view = 100003805494149 # me
# id_view = 1743946585784385 # test
# id_view = 1815997055246004 # test , 41
id_view = 515225773163146  # test

# Start worksheet
wb = Workbook()
token = "Your FB token"
payload = {"method": "GET", "access_token": token}
print("Processing...")
# a = requests.get("https://graph.facebook.com/" + str(id_view) + "/feed",params=payload).json()
a = requests.get("https://graph.facebook.com/" + str(id_view) +
                 "/comments?limit=1000", params=payload).json()

while True:
    data = a['data']
    # Lấy comment
    for i in range(len(data)):
        name = a['data'][i]['from']['name']
        text = a['data'][i]['message']
        cmt_ID = a['data'][i]['id']
        # print("{:<30} {:<15}".format(name,text))
        log.append(text)
        sender.append("("+str(name)+")")
        total = total+1
        # Cố gắng lấy toàn bộ reply
        try:
            r = requests.get('https://graph.facebook.com/' +
                             cmt_ID + '/comments?limit=500', params=payload).json()
        except Exception as e:
            raise e
            break
        rep = r['data']
        for j in range(len(rep)):
            name = rep[j]['from']['name']
            reply = rep[j]['message']
            cmt_ID = rep[j]['id']
            # print(cmt_ID)
            # print(">> {:<30} {:<15}".format(name,text))
            log.append(" >> "+str(reply))
            sender.append("(từ "+str(name)+")")
            total = total+1
    break
# Show Ket qua
# for x in range(len(log)):
# 	print(log[x],sender[x])
print("Total message: ", total)

# ----------- Phần trên OK rồi, k chỉnh gì nữa nha :< -------------
# Luu ra excel
# sheet1 = wb.add_sheet('sheet 1')
sheet1 = wb.add_sheet('Sheet 1', cell_overwrite_ok=True)
# Title
sheet1.write(0, 0, 'From')
sheet1.write(0, 1, 'Message')
sheet1.write(0, 2, 'Today: ' + str(time_now))
sheet1.write(1, 2, 'Tổng: ' + str(total))
# Start export to excel
# From
row = 1
col = 0
for item in (sender):
    sheet1.write(row, col, item)
    row += 1
# Message
row = 1
col = 1
for item in (log):
    if len(item) < 1000:
        sheet1.write(row, col, item)
    else:
        sheet1.write(row, col, item[:200])
    row += 1
# wb.save(filename + '.xls')
wb.save('viewme.xls')
print("Done ", total)
exit()
# ----Output--------
# Processing...
# Total message:  90
# Done  90