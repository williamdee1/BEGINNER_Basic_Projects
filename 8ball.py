import random as rand
import time

def read_file ( file ):
    with open(file, 'r', encoding = "utf8") as f:
        lines = f.readlines()
    return lines

file = read_file("8ball.txt")

play = True

def eightball():
	input("\nAsk me anything...\n\n...> ")
	response = rand.choice(file)
	print("\n\n...",response)
	replay()


def replay():
	again = input("\nWould you like to ask another question?\n\n...>")
	if again in ("Yes", "Y", "yes", "y"):
		eightball()
	elif again in ("No", "N", "no", "n"):
		exit()
	else:
		print("\nIt's a yes or no answer... try again...")
		time.sleep(1)
		replay()

eightball()
	
	

