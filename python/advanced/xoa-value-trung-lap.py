mylist = ["a", "b", "a", "c", "c"]
mylist = list(dict.fromkeys(mylist))
print(mylist)
# return ['a', 'b', 'c']
# Tạo từ điển, sử dụng Danh sách các mục làm khóa. Thao tác này sẽ tự động loại bỏ mọi bản sao vì từ điển không thể có các khoá trùng lặp.
# -------Output-----------
# ['a', 'b', 'c']