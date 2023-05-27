import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

list_of_options = [rock,paper,scissors]

user_option = int(input("What do you choose? Type 0 for Rock, 1 for Papel and 2 for Scissors.\n"))

if user_option >= 3 or user_option < 0:
    print("Invalid Option! Choose an option between 0 and 2.")
else:
    computer_option = random.randint(0,len(list_of_options) - 1)

    print(list_of_options[user_option])

    print("Computer chose\n" + list_of_options[computer_option])


    if list_of_options[user_option] == rock and list_of_options[computer_option] == scissors:
        print("You win!")
    elif list_of_options[user_option] == paper and list_of_options[computer_option] == rock:
        print("You win!")
    elif list_of_options[user_option] == scissors and list_of_options[computer_option] == paper:
        print("You win!")
    elif list_of_options[user_option] == list_of_options[computer_option]:
        print("Draw!")
    else:
        print("You lose!")







