import random

open_file = open("Dictionary.txt", "r")
list = []


wordGenerator = open_file.readline()

while wordGenerator != "":
        list.append(wordGenerator)
        wordGenerator = open_file.readline()
num  = len(list) - 1
random = random.randint(0, num)
print("Here is a random word!")
print(list[random])
