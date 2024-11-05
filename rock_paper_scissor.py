import random
print("Welcome to the game ROCK PAPER SCISSOR")
choice_list = ["rock","paper","scissor"]
user_wins = 0
computer_wins = 0
while True:
    your_choice = input("please enter your input rock/paper/scissor/Q : ").lower()
    computer_input = random.randint(0,2)
    computer_choice = choice_list[computer_input]
    if your_choice == "q":
        print("You ended the game") 
        break
    elif(your_choice.lower() not in choice_list):
        continue
    elif your_choice == "rock" and computer_choice == "scissor":
        print("You won!!!")
        user_wins += 1
    elif your_choice == "paper" and computer_choice == "rock":
        print("You won!!!")
        user_wins += 1
    elif your_choice == "scissor" and computer_choice == "paper":
        print("You won!!!")
        user_wins += 1
    elif your_choice == computer_choice:
        print("Match tied")
    else:
        print("You lost! Computer Won!!!")
        computer_wins += 1
print("Computer won",computer_wins,"times.")
print("You won",user_wins,"times.")
