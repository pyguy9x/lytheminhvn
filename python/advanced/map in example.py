num = 123456

# Sử dụng map
list_of_digits = list(map(int, str(num)))
print(list_of_digits)
# Sử dụng map
text = "today i go to school"
def tach(t):
    r = ""
    for x in t.split(" "):
        r+=str(x)
    return r

list_of_text = list(map(tach,text))
print(list_of_text)
# Sử dụng list comprehension
list_of_text2 = [x for x in str(text)]
print(list_of_text2)
# Sử dụng lamda
list_of_text3 = list(map(lambda x:x,text))
print(list_of_text3)


list_goc = [10, 9, 8, 7, 6, 1, 2, 3, 4, 5]

#list_moi = list((lambda a: a*2 , list_goc))
#output is [<function <lambda> at 0x03621E88>, [10, 9, 8, 7, 6, 1, 2, 3, 4, 5]]
list_moi = list(map(lambda a: a*a , list_goc))
# Kết quả: [20, 18, 16, 14, 12, 2, 4, 6, 8, 10]
# By Quantrimang.com
print(list_moi)

a = [1,2,3,4]
b = list(map(int,a))
print(b)
b = list(map(str,a))
print(b)
b = list(map(str,text))
print(b)
# -------Output-----------
# [1, 2, 3, 4, 5, 6]
# ['t', 'o', 'd', 'a', 'y', '', 'i', '', 'g', 'o', '', 't', 'o', '', 's', 'c', 'h', 'o', 'o', 'l']
# ['t', 'o', 'd', 'a', 'y', ' ', 'i', ' ', 'g', 'o', ' ', 't', 'o', ' ', 's', 'c', 'h', 'o', 'o', 'l']
# ['t', 'o', 'd', 'a', 'y', ' ', 'i', ' ', 'g', 'o', ' ', 't', 'o', ' ', 's', 'c', 'h', 'o', 'o', 'l']
# [100, 81, 64, 49, 36, 1, 4, 9, 16, 25]
# [1, 2, 3, 4]
# ['1', '2', '3', '4']
# ['t', 'o', 'd', 'a', 'y', ' ', 'i', ' ', 'g', 'o', ' ', 't', 'o', ' ', 's', 'c', 'h', 'o', 'o', 'l']