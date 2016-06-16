import random
import time

# Just a fun, trivial program that simulates rolling a dice, will be used in further, more advaced programming projects.
class Dice:
	def __init__(self):
		roll = 0

	def rollDice(self, seed):
		random.seed(seed)
		roll = random.randint(1, 6)
		print("Rolling...")
		print("_______")
		print("|     |")
		print("|  *  |")
		print("|_____|")
		time.sleep(1)
		print("_______")
		print("|  *  |")
		print("|  *  |")
		print("|_____|")
		time.sleep(1)
		print("_______")
		print("|  *  |")
		print("|  *  |")
		print("|__*__|")
		time.sleep(1)
		print("_______")
		print("| * * |")
		print("| * * |")
		print("|_____|")
		time.sleep(1)
		print("_______")
		print("| * * |")
		print("| * * |")
		print("|__*__|")
		time.sleep(1)
		print("_______")
		print("| * * |")
		print("| * * |")
		print("|_*_*_|")
		time.sleep(1)
		print("Your roll is: %i" % roll)
		if roll == 1:
			print("_______")
			print("|     |")
			print("|  *  |")
			print("|_____|")
		elif roll == 2:
			print("_______")
			print("|  *  |")
			print("|  *  |")
			print("|_____|")	
		elif roll == 3:
			print("_______")
			print("|  *  |")
			print("|  *  |")
			print("|__*__|")	
		elif roll == 4:
			print("_______")
			print("| * * |")
			print("| * * |")
			print("|_____|")			
		elif roll == 5:
			print("_______")
			print("| * * |")
			print("| * * |")
			print("|__*__|")
		else:
			print("_______")
			print("| * * |")
			print("| * * |")
			print("|_*_*_|")
	def resetDice(self):
		roll = 0

def invalidInput():
	print("Invalid input, only answer with 'Y' or 'N'")
	still_Rolling = input("Do you want to roll the dice? (Y/N) ").upper()
	return still_Rolling

still_Rolling = input("Do you want to roll the dice? (Y/N) ").upper()
while still_Rolling not in ['Y', 'N']:
	still_Rolling = invalidInput()

while still_Rolling == 'Y':
	dice = Dice()
	seed = input("What seed do you want to use? ")
	while seed.isdigit() == False:
		print("You may only enter a digit for the seed, try again.")
		seed = input("What seed do you want to use? ")
	dice.rollDice(seed)
	still_Rolling = input("Do you want to roll again? (Y/N) ").upper()
	while still_Rolling not in ['Y', 'N']:
		still_Rolling = invalidInput()

print("Thanks for playing!")