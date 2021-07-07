x = (1,2,3)
print(x)
print(*x)
print("-"*30)

list1 = [1, 2, 3]
list2 = [4, 5]
list3 = [6, 7, 8, 9]
x = [*list1, *list2, *list3]
print(x)

print("-"*30)
y = [y for y in enumerate(x)]
print(y)
print("-"*30)

dict1 = {"A": 1, "B": 2}
dict2 = {"C": 3, "D": 4}
x = {**dict1, **dict2}
print(x)
print("-"*30)

list4 = [1,2,3,4,5,6]
a,*b,c=list4
print(a)
print(*b)
print(c)
