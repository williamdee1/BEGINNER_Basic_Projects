import random as rand

pc_guess = rand.randint(1, 21)

guess = int(input("Please guess a number between 1 and 20:"))
n = 0

while pc_guess != guess:
    n = n + 1
    print("Sorry that was not the number I was thinking of...\n")
    if pc_guess > guess:
        guess = int(input("Please try a larger number:"))
    elif pc_guess < guess:
        guess = int(input("Please try a smaller number:"))
    else:
        break

print("Well done, you guessed correctly!")
print("The number I was thinking of was: ", pc_guess)
print("You took ", n, " attempts to guess correctly")