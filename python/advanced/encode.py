# -*- coding: utf-8 -*-
s = input("Nhập chuỗi:> ") or "xin chào"
v = s.encode()
print(v)
n = v.decode()
print(n)