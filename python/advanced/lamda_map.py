number = (1,2,3,4)
ketqua = map(lambda x: x*x,number)
 
# chuyen map object thanh list
print(list(ketqua))
 
#return  [1, 4, 9, 16]

dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]
 
 
name  = map(lambda x: x['name'], dict_a)  # Output: ['python', 'java']
print(list(name))
 
point = map(lambda x: x['points'] * 10, dict_a)  # Output: [100, 80]
print(list(point))