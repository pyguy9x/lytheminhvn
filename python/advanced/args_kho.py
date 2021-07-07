# coding: utf-8
# *args: đầu vào bao nhiêu cũng được, xử lí với list
def foo(numbers):
    result = 0
    for n in numbers:
        result += n
    return result
print(foo([1, 2]))
print(foo([1, 2, 3]))
'''
Cách làm này khá hiệu quả, ngoại trừ một bất tiện nhỏ là chúng ta cần tạo ra một list các số cần tính toán. Điều này khá bất tiện trong các bài toán thực tế hơn, do các số cần tính toán nà nhiều khi cũng biến động chứ không cố định.
Đây là lúc là cú pháp *args cực kỳ hữu ích, bởi nó cũng giúp chúng ta có thể truyền một số lượng tham số tuỳ ý vào hàm:
'''
def foo(*numbers): # chú ý, *args = *numbers
    result = 0
    for n in numbers:
        result += n
    return result
print("new: ",foo(1, 2)) # chú ý, ko có dấu cặp dấu []
print("new: ",foo(1, 2, 3)) # chú ý, ko có dấu cặp dấu []
'''
Cú pháp này tiện lợi hơn rất nhiều do chúng ta hoàn toàn không cần xây dựng một list để truyền vào hàm. Tất cả các tham số truyền vào sẽ là phần tử của args và chúng ta có thể duyệt qua nó như một tuple bình thường.
'''
def foo(a,b,*numbers): # chú ý, *args đặt ở cuối
    # Nguyên nhân là do *args sẽ nhận toàn bộ các tham số "còn lại" sau khi các tham số đầu tiên đã có giá trị, do đó, các tham số phía sau *args sẽ không bao giờ được truyền vào nữa.
    print("normal var ",a,b)
    for n in numbers:
        print('*args var ',n)
foo(4,6,7,8)
# -------Output-----------
# 3
# 6
# new:  3
# new:  6
# normal var  4 6
# *args var  7
# *args var  8