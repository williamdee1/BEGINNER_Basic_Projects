import random as rand
import time

print("Hello, let's play a game of Rock, Paper, Scissors.\n")
print("Please make your guess after I count down\n")
time.sleep(1)
print("Rock")
time.sleep(1)
print("Paper")
time.sleep(1)
print("Scissors\n")

rps = ["Rock", "Paper", "Scissors"]
pc_choice = rand.choice(rps)

guess = input().capitalize()
n = 0

while n < 10:
	time.sleep(1)
	n = n + 1
	if guess in rps:
		if guess == "Rock":
			if pc_choice == "Paper":
				print("\n---Paper covers rock, you lose!")
				break
			if pc_choice == "Scissors":
				print("\n---Rock bashes Scissors, you win...")
				break
			if pc_choice == "Rock":
				guess = input("\nWe chose the same, please guess again...").capitalize()
				pc_choice = rand.choice(rps)
		elif guess == "Paper":
			if pc_choice == "Rock":
				print("\n---Paper covers Rock, I lose...")
				break
			if pc_choice == "Scissors":
				print("\n---Scissors cuts paper, I win!")
				break
			if pc_choice == "Paper":
				guess = input("\nWe chose the same, please guess again...").capitalize()
				pc_choice = rand.choice(rps)
		elif guess == "Scissors":
			if pc_choice == "Rock":
				print("\n---Rock bashes Scissors, I win!")
				break
			if pc_choice == "Paper":
				print("\n---Scissors cuts paper, I lose...")
				break
			if pc_choice == "Scissors":
				guess = input("\nWe chose the same, please guess again...").capitalize()
				pc_choice = rand.choice(rps)
	elif guess not in rps:
		guess = input("\nPlease guess either Rock, Paper or Scissors!").capitalize()
	else:
		break


print("\nMy guess was", pc_choice)