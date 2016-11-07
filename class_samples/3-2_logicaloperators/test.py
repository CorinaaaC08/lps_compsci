# number 2

#this will print and ask how old is the user
print("How old are you?")

#this will allow the user to input their age and turn it into an integer
age = int(input())

#print and ask the user how old they are
print("How many inches tall are you?")

#allow user to input height and convert it into integer
height = int(input())

#it will print to user that they are old and tall enough to ride if they are older than 10 and taller than 50
if age > 10 and height > 50:
	print("Hooray! You're old enough and tall enough to ride.")
#if they are not older than 10 nor taller than 50 inches than it will print that they can't ride
else:
	print("Sorry, you can't ride.")
