# -*- coding: utf-8 -*-

# sublime text k hỗ trợ input

s = input("Nhập chuỗi:> ") or "xin chào"
v = s.encode()
print(v)
n = v.decode()
print(n)
