print('How many miles do you live from Richmond?')
miles = int(raw_input())

print('What is your GPA?')
GPA = float(raw_input())

if GPA  > 3.0 and miles > 30:
	print('Congrats, welcome to Columbia!')

if GPA <= 3.0 or miles <= 30:
	print('Sorry, good luck at Harvard.')
