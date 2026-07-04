import random
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))

computer_input = random.randint(0, 2)
print(f"the computer chose {computer_input}")

if user_input >= 3 or user_input < 0:
    print("Incorrect values you lose")
elif user_input == computer_input:
    print("Draw")

elif ((user_input == 0 and computer_input == 1) or
      (user_input == 1 and computer_input == 2) or
      (user_input == 2 and computer_input == 0)):
    print("Computer wins")

else:
    print("You win")