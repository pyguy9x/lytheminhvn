dict_1 = {'apple': 9, 'banana': 6}
dict_2 = {'banana': 4, 'orange': 8}

def mergeDict(dict1, dict2):
   ''' Hợp nhất dictionaries và giữ giá trị của key phổ biến trong list'''
   dict3 = {**dict1, **dict2}
   for key, value in dict3.items():
       if key in dict1 and key in dict2:
               dict3[key] = [value , dict1[key]]
 
   return dict3

# Hợp nhất dictionaries và thêm giá trị của key phổ biến trong list
dict3 = mergeDict(dict_1, dict_2)
 
print('Dictionary 3 :')
print(dict3)
print('banana 1st element: ',dict3['banana'][0])