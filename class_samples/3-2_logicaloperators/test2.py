print('How many miles do you live from Richmond State?')
miles = int(raw_input())

print('What is your GPA?')
GPA = float(raw_input())

print('What is your Act score?')
Act = int(raw_input())

if miles <=  30 and GPA >= 2.0 or miles > 30 and GPA >= 2.5 and Act >= 18: 
	print('Welcome to Richmond State!')
else:
	print('Sorry, you were not accepted.')

