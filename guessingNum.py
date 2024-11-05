import random
no_of_guesses = 0
high_range = input("Please enter the higher boundary: ")
if(high_range.isdigit()):
    high_range = int(high_range)
else:
    print("Please Enter the Number.The input you entered is not a number")
    quit()
num = random.randint(0,high_range)
while True:
    no_of_guesses +=1
    guess = input("Please guess the number: " )
    if(guess.isdigit()):
        guess = int(guess)
    else:
        print("please enter number!!!")
    if(guess == num):
            print("You guessed it Right")
            break
    elif(guess > num):
            print("your guess greater than num")
    else:
            print("your guess is less than num")
    
print("you guessed in",no_of_guesses,"guesses")