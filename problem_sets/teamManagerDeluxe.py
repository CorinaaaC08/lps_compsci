#creates player class which has name, age, goals, jersey_number, and position of player
class Player (object):
	def __init__(self, name, age, goals, jersey_number, position ):
                self.name = name
                self.age = age
                self.goals = goals
		self.jersey_number = jersey_number
		self.position = position
#allows user to get summary of player 
	def getStats(self):
                summary = "Name: " + self.name + '\n'
                summary = summary + "Age: " + str(self.age) + '\n'
                summary = summary + "Goals: " + str(self.goals) + '\n'
		summary = summary + "Jersey Number:" + str(self.jersey_number) + '\n'
		summary = summary + "Position:" + self.position
	
#this loads an existing file
def LoadTeam(playerList,filename):
       file = open(filename,"r")
       myReadLine = file.readline()
       while myReadLine != " ":
       		y = myReadLine.split(" ")
       		z = Player(y[0],str(y[1]), str(y[2]), str(y[3]), y[4])
       		playerList.append(z)
		myReadLine = file.readline()
       file.close()
#allows user to save the team by writing the player's info to the file
def saveTeam(playerList, filename):
       file = open(filename, 'a')
       for player in playerList:
       		file.write(player.name + " " + str(player.age) + " " + str(player.goals) + " " +
str(player.jersey_number) + " " + player.position + "\n")
       file.close()

list = []
#asks the user whether they want to start a new team or open an existing one
print('Do you want to start with a new team or open an existing team?')
print('(1) Start with a new team')
print('(2) Open a file for an existing team')
x = raw_input()
# this wll allow you to load the file for an existing team by calling out the LoadTeam  
if x == "2": 
	print("What's the filename for your exisiting team? Enter the whole name, including its .tmd extension.")
        z = raw_input()
        LoadTeam(list,z)

#x allows  the while loop to run 
x = True
while x == True:
	#asks the user what they want to do
        print("What do you want to do?")
        print('(1)Add Player')
        print('(2)Print Players')
	print('(3)Save your player list to a file')
	print('(0) Leave the program (save first to avoid losing your data')
        y = int(raw_input())
	#creates variables for all the info that they enter and adds it to the myPlayer list
        if y ==  1:
                print('Enter a Name')
               	user_enteredname = raw_input()
                print('Enter Age')
                user_enteredage = raw_input()
                print('Enter number of goals')
                user_enteredgoals = raw_input()
		print('Enter jersey number')
		user_enterednumber = raw_input()
		print('Enter position')
		user_enteredposition = raw_input()
                myPlayer = Player(user_enteredname, user_enteredage, user_enteredgoals,user_enterednumber, user_enteredposition)
                list.append(myPlayer) 
	#prints players in  list
	elif y == 2:
        	for l in list:
	        	print(l.getStats())
	#allows user to save the file with the player 
	if y == 3:
		print("What would you like to call your file?")
		filename = raw_input()
		saveTeam(list, filename)
	#closes the app
	elif y == 0:
		exit()


