# class gốc
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        self.gotmarks = self.name + ' obtained ' + self.marks + ' marks'

st = Student("Jaki", "25")

print(st.name) # Jaki
print(st.marks) # 25
print(st.gotmarks) # Jaki obtained 25 marks

# Giờ muốn đổi tên Jaki thành Nata thì sao?
st.name = "Anusha"
print(st.gotmarks)
# Jaki obtained 25 marks
# vẫn vậy k thay đổi !
# Giải pháp :dùng @properties
print("-- This")
class Student_new:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    @property #<< chú ý. Nghĩa là hàm ở dưới sẽ đc update khi giá trị thay đổi
    def gotmarks(self):
        return self.name + ' obtained ' + self.marks + ' marks'


st = Student_new("Nata", "25")
print(st.gotmarks)
st.name = "Karol"
print(st.gotmarks)

