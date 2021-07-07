# Ví dụ về enumerate

# Sử dụng list prehension
li = [int(x) for x in range(5)]
print(li)

# Sử dụng enumerate
li = [0,8,2,3,6]
# a = [x for x in enumerate(li)]
a = [x for i,x in enumerate(li)]
# show value
print(a)

# show index
b = [i for i,x in enumerate(li)]
print(b)
# -------Output-----------
# [0, 1, 2, 3, 4]
# [0, 8, 2, 3, 6]
# [0, 1, 2, 3, 4]