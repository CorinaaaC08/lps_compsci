#this allows for the computer to choose the magic number and assigns guess a random number for the code to run
#the print statement allows for the user to see what the game is about 
import random
mynum = random.randint(1,1000)
guess = 1 
print('I am thinking of a number between 1 and 1000. Enter your guess!') 

#it allows for the code to run while the guess that is made is less than 1000
while guess <= 1000 :	
	guess = int(raw_input())
#if the user's guess is less than mynum then it will tell them that there guess is too low and makes them guess again
#if it is greater than mynum then it will tell them that there guess is too high
#if it equals mynum than it will tell the user they won and ends the code
	if guess < mynum:
		print('Nope too low!. Guess again.')
	elif guess > mynum: 
		print('Nope too high! Guess again.')	
	else: 
		print('You win!')
		break
