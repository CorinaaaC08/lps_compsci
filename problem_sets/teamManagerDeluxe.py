print('Welcome to Team Manager Deluxe!')
print('Do you want to start with a new team or open an existing team?')
print('(1) Start with a new team')
print('(2) Open a file for an existing team')
x = raw_input()
# this iwll alloow you to add user 
if x == 1: 
	#don't ask them to create a new file unless they want to save the file 
	myPlayers = []
	x = True
	while x == True:
        	print("What do you want to do?")
        	print('(1)Add Player')
        	print('(2)Print Players')
		print('(3)Save your player list to a file')
		print('(0) Leave the program (save first to avoid losing your data')
        	y = int(raw_input())
        	if y ==  1:
                	print('Enter a Name')
                	user_enteredname = raw_input()
                	print('Enter Age')
                	user_enteredage = raw_input()
                	print('Enter number of goals')
                	user_enteredgoals = raw_input()
                	myPlayer = Player(user_enteredname, user_enteredage, user_enteredgoals)
                	myPlayers.append(myPlayer) 
		elif y == 2:
        	        for l in myPlayers:
	                        print(l.getStats())
		if y == 3:
			def saveTeam(playerlist, filename):
        			file = open(filename, 'w')
        			file.write(user_enteredname)
				file.write(user_enteredage)
				file.write(user_enteredgoals)
				file.close()
		elif y == 0:
			filename.close()






elif x == 2:	
	print("What's the filename for your exisiting team? Enter the whole name, including its .tmd extension.")
	file = raw_input()
	def LoadTeam(filename):
		x = open(filename,'r')
	class Player (object):
		def __init__(self, name, age, goals):
			self.name = name 
			self.age = age
			self.goals = goals
		def getStats(self):
			summary = "Name: " + self.name + '\n'
			summary = summary + "Age: " + str(self.age) + '\n'
			summary = summary + "Goals: " + str(self.goals)
			return summary
		filename.close()

	

