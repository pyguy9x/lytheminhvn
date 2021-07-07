# **kwargs: đầu vào bao nhiêu cũng được, xử lí với dict
def foo(a=0, b=1):
    return a + b
print(foo())
# 1
print(foo(1, 2))
# 3
print(foo(b=3, a=4))
# 7
def foo(a):
    for key, value in a.items():
        print(key, value)
foo({'a': 1, 'b': 2})
# a 1
# b 2
print('{0:_^31}'.format("kwargs")) # màu mè tí =))
def foo(**test):
    for key, value in test.items():
        print(key, value)
foo(a=1,b=2)
print('--------args and kwargs-----') # màu mè tí =))
def foo(a,b,*args,**kwargs):
    result = ""
    print("normal ",a,b)
    for i in args:
        print("args ",i)
    for j,k in kwargs.items():
        print(f"kwargs {j}:{k}")
        result += j
        # if result += k line34 will return "cef"
    return result
        
foo(1,2,5,7,8,3,x1="c",x2="e",x3="f")
print("=> result ",foo(5,5,anh="c",nho="e",em="f"))
# -------Output-----------
# args  5
# args  7
# args  8
# args  3
# kwargs x1:c
# kwargs x2:e
# kwargs x3:f
# normal  5 5
# kwargs anh:c
# kwargs nho:e
# kwargs em:f
# => result  anhnhoem