# Import các thư viện
from datetime import datetime
from datetime import date
 
today = datetime.today()
 
# Lấy số ngày trong tuần
wd = date.weekday(today)
# Tạo danh sách tên các thứ trong tuần
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
 
# In ra kết quả
print('Today is day number', wd)
print('which is a', days[wd])
# -------Output-----------
# Today is day number 2
# which is a Wednesday