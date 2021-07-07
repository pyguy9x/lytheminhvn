def foo(a,b,*args,**kwargs):
    result = ""
    print("normal ",a,b)
    for i in args:
        print("args ",i)
    for j,k in kwargs.items():
        print(f"kwargs {j}:{k}")
        result += k
        # if result += j line34 will return <key><key>...<key>
    return result
text = foo(1,2,3,4,5,6,c1="this ",
           c2="is ",c3="awesome ",)
print(text)




