'''
Using *args to import
Coded by: Ly The Minh
All rights reserved (C) July-2021
'''
inputs = ['Mot','hai','ba','bon','nam']
string = 'Hom nay toi gap {0} nguoi qua duong, toi xin ho {1} dollar de mua {2} chiec banh mi. Bat ngo {3} nguoi ban cua toi den va dua cho toi {4} cai banh pizza that dep.'.format(*inputs)
print(string)
# Output
# Hom nay toi gap Mot nguoi qua duong, toi xin ho hai dollar de mua ba chiec banh mi. Bat ngo bon nguoi ban cua toi den va dua cho toi nam cai banh pizza that dep.