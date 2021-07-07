# Chèn
ngay = ['number 1', 'number 2', 'number 3', 'number 5']
print(ngay)
ngay.insert(3, 'number 4')     # chèn vào vị trí thứ 3
print(ngay)
# Xóa phần tử từ 0 đến 2
del ngay[0:3]
print(ngay, "*")
# Xóa phần tử chỉ định
ngay.remove('number 4')
print(ngay, "**")
# Xóa toàn bộ list
del ngay
# Lồng
ngaysinh = [13, 9, 2000]
thongtin = ['nguyen van a', ngaysinh]

ngay = thongtin[1]
print(ngay[0])
print(thongtin[1][0])  # hoặc cũng có thể viết ngắn gọn lại như vậy

# Return index of element
animals = ['cat', 'dog', 'fish', 'cow', 'goat']
fish_index = animals.index('fish')
print(fish_index)  # return 2
# Sort
numbers = [6, 2, 4, 3, 5, 1]
numbers.sort()
print(numbers)

# Reverse sort
values = [2, 10, 7, 14, 50]

# To sort the values in descending order:
values.sort(reverse=True)
print(values)

# Count
lst = [1, 2, 3, 4, 5, 6, 1, 4, 5, 2]
print(lst.count(1))  # return 2, there are two number 1 in list
print(lst.count(3))  # return 1, there is only one number 3 in list

# Reverse list
print(lst[::-1])
# -------Output-----------
# ['number 1', 'number 2', 'number 3', 'number 5']
# ['number 1', 'number 2', 'number 3', 'number 4', 'number 5']
# ['number 4', 'number 5'] *
# ['number 5'] **
# 13
# 13
# 2
# [1, 2, 3, 4, 5, 6]
# [50, 14, 10, 7, 2]
# 2
# 1
# [2, 5, 4, 1, 6, 5, 4, 3, 2, 1]