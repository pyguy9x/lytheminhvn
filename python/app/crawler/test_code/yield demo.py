# Hàm in các số chẵn từ mảng arr
def in_so_chan(arr):
    for i in arr:
        if i % 2 == 0:
            yield i
 
# Chương trình chính
mang = [1,4,2,3,5,5,654,66,76,87,8]
sochan = in_so_chan(mang)
print(next(sochan))
print(next(sochan))
for i in sochan:
	print(i)