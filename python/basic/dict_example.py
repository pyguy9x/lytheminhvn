# Ví dụ về dictionary

# Từ điển gốc
Dict = {'hieu': 17, 'hoai': 18, 'anh': 22, 'nam': 25}

Dict.update({'hieu': 16})  # cập nhật tuổi cho 'hieu'
Dict.update({'thu': 26})  # thêm một phần tử mới

print(Dict)

dict = {1: 'a', 5: 'h', 3: 'x', 2: 'l'}
# Sắp xếp tăng dần theo key
print(sorted(dict.items(), reverse=False))
# return [(1, 'a'), (2, 'l'), (3, 'x'), (5, 'h')]

# Sắp xếp giảm dần theo key
print(sorted(dict.items(), reverse=True))
# return [(5, 'h'), (3, 'x'), (2, 'l'), (1, 'a')]

dict = {1: 'a', 5: 'h', 3: 'x', 2: 'l'}
s = []
# sắp xếp tăng dần theo giá trị của key
for i in sorted(dict, key=dict.get, reverse=False):
    s.append((i, dict[i]))

print(s)
# return [(1, 'a'), (5, 'h'), (2, 'l'), (3, 'x')]
# -------Output-----------
# {'hieu': 16, 'hoai': 18, 'anh': 22, 'nam': 25, 'thu': 26}
# [(1, 'a'), (2, 'l'), (3, 'x'), (5, 'h')]
# [(5, 'h'), (3, 'x'), (2, 'l'), (1, 'a')]
# [(1, 'a'), (5, 'h'), (2, 'l'), (3, 'x')]
