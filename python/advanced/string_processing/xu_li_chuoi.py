'''
String Processing
Coded by: Ly The Minh
All rights reserved (C) July-2021
'''
string = 'Dogs are love'
print("d o g s _ a r e _ l  o  v  e")
print("0 1 2 3 4 5 6 7 8 9 10 11 12")
print()
print("  d   o   g  s  _   a  r  e  _  l  o  v  e")
print("-13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1")
print()
print(string[5:13], ' => [5:13]')  # Lấy từ trái sang, từ vị trí 5 đến 13-1=12
print(string[5::], ' => [5::]') # Lấy từ 5 đến hết
print(string[5:11], ' => [5:11]')
print(string[1::2], ' => [1::2]') # Lấy từ 1, nhảy 2 đơn vị
print(string[1:12:5], ' => [1:12:5]') # Lấy từ 1 đến 12-1=11, nhảy 5 đơn vị
print(string[-4:], ' => [-4:]')  # Lấy từ trái sang, từ vị trí -4
print(string[:-5], ' => [:-5]')  # Lấy từ trái sang, từ vị đầu đến -5
# Lấy tất cả, từ trái sang, từ vị -8 đến -5-1=-6
print(string[-8:-5], ' => [-8:-5]')
print(len(string))
print("--Ung dung thuc te--")
name = "chrome_image_picture.png"
print("Name of %s is: %s" % (name,name[:-4]))

# Get the 't' of list
list = [1, ['a', 'b', ['kill', 'bat', 'cup'], 'c'], 3]
print(list[1][2][1][2])
# Output
# d o g s _ a r e _ l  o  v  e
# 0 1 2 3 4 5 6 7 8 9 10 11 12

#   d   o   g  s  _   a  r  e  _  l  o  v  e
# -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1

# are love  => [5:13]
# are love  => [5::]
# are lo  => [5:11]
# osaelv  => [1::2]
# orv  => [1:12:5]
# love  => [-4:]
# Dogs are  => [:-5]
# are  => [-8:-5]
# 13
# --Ung dung thuc te--
# Name of chrome_image_picture.png is: chrome_image_picture
# t