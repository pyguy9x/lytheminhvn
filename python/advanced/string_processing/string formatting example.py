print('Hello, my name is {my_name:s}. I am {my_age:d} years old'.format(my_name = "Foo", my_age = 25))

test = '{:<30}'.format('left aligned')
print(test)                
test = '{:>30}'.format('right aligned')
print(test)
test='{:<30} {:>30}'.format('left aligned', 'right aligned')    
print(test)
test = '{:+^30}'.format(' centered ')
print(test)
# Add decimal point
test = '{:,}'.format(1234567890)
print(test)
# Print binary number
test = '{0:#b}'.format(95)
print(test)
# Print float number
points = 19
total = 22
print('Correct answers: {:.2%}'.format(points/total))
# 'Correct answers: 86.36%'
# Mail merge
from string import Template
t = Template('Dear, $name! On behalf of Python Geeks, welcome you onboard!')
users = ["Mark", "David", "Hen"]
for user in users:
	print(t.substitute(name=user))
# 'Dear, Mark! On behalf of Python Geeks, welcome you on board!'
# 'Dear, David! On behalf of Python Geeks, welcome you on board!'
# 'Dear, Hen! On behalf of Python Geeks, welcome you on board!'