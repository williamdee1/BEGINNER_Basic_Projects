import random as rand
import string

print("Thank you for using the random password generator\n")

n = int(input("Please specify how many characters you'd like in your password\n"))

list = string.ascii_letters + string.digits

password = ''.join(rand.choices(list, k=n))

print("\nYour new password is: ", password)

use = input("\nWhat will this be used for?\n")


f = open("passwords.txt", "a")
f.write("\n")
f.write(use)
f.write("\n")
f.write(password)
f.close

print("\nYour password has been saved in passwords.txt")