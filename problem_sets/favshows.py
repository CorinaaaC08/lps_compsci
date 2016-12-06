print('Welcome to Pumapix!')
print("Enter your 5 favorite shows.")
showlist = []
x = 1
while x <= 5:
	print('Enter a show name:')
	showlist.append(raw_input())
	x = x + 1 
print('ok here is what you entered:') 
print(showlist)

print('We have addded a couple of important ones.')

myshows = ["Breaking Bad", "The Wire"]
total = showlist + myshows
total.sort()
sum = 0 
for y in total:
	sum = sum + 1
	print(str(sum) + '. '  + y)
