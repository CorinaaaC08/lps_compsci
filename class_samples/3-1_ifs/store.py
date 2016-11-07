fave = 8
print("Let's play a game!")
print('Try to guess my favorite number!') 
print('Enter a number')
x = int(raw_input())
if x > 8:
	print('Sorry, you lose')
if x <= 8:
	print('Hooray, you won! Good choice.')


