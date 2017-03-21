x = 'True'
contact_info = {}
while True:
	print('(1)Add a phone number')
	print('(2)Print the full list of contacts')
	print("(3) Enter a name to retrieve the that contact's phone number")
	print('(4) Exit the Contacts App')
	x = int(raw_input())
	if x == 1:
		print("Enter a name")
		name = raw_input()
		print('Enter a phone number')
		number = raw_input()
		contact_info[name] = number	
	elif x == 2:
		print(contact_info)
	elif x == 3:
		print("Enter a name")
		y = raw_input()
		print(contact_info[y])
	elif x == 4:
		exit()
