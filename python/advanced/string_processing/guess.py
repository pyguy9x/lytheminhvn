'''
String Processing: Get the attendee on event
Coded by: Ly The Minh
All rights reserved (C) July-2021
'''
def guess_list(attendees):
	return [name.split(' ')[0] for name in attendees]

attendees = ['Ha Ho', 'Trang Tran', 'Jennifer Pham','Victor Vu']
print(guess_list(attendees))

# Output
# ['Ha', 'Trang', 'Jennifer', 'Victor']