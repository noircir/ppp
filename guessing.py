import random

random_number = random.randint(1,10)  # numbers 1 - 10
guess = None
play_again = "yes"

while (play_again == "yes"):
	while guess != random_number:
		guess = input("Pick a number from 1 to 10: ")
		guess = int(guess)
		if guess < random_number:
			print("TOO LOW!")
		elif guess > random_number:
			print("TOO HIGH!")
		else:
			print("YOU WON!!!!")

	print("===============================")
	play_again = input("Would you like to continue? yes/no: ")
	if play_again == "no":
		break




#print(random_number)

# handle user guesses
#   if they guess correct, tell them they won
#     otherwise tell them if they are too high or too low

# BONUS - let player play again if they want!