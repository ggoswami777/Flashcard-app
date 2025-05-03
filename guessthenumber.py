import random
def guess(x):
    random_number = random.randint(1, x)
    guess=0
    while(guess!=random_number):
        guess=int(input(f"Guess a number between 1 and {x} :"))
        if guess<random_number:
            print("Sorry,Guess again, Too low.")
        elif guess>random_number:
            print("Sorry,Guess again, Too high.")

    print(f"Yay,congrats you have guessed the random number correctly!  {guess}")

def computer_guess(x):
    low=1
    high=x
    feedback=" "
    while feedback!="c":
        if low!=high:
            guess=random.randint(low,high)
        else:
            guess=low
        feedback=input(f"Is {guess}, Too high (H),Too low (L) or correct (C)??").lower()
        if feedback=="h":
            high=guess-1
        if feedback=="l":
            low=guess+1
    print(f"Yay! The Computer guessed your number,{guess} correctly.")

play_again="yes"
while play_again.lower() in ["yes","y"]:
    print("Let's start the game!")
    n=int(input("Enter 1 : If you want to guess the number\n Enter 2 : If you want computer to guess the number \n"))
    if n==1:
        x=int(input("Maximum number till which you can guess:"))
        guess(x)
    elif n==2:
        x=int(input("Enter the maximum number till which the computer can guess up too:"))
        print("Think a number in your mind and let the computer guess it")
        computer_guess(x)
    else:
        print("Invalid choice ")
    play_again=input("\n Do you want to play again? (yes/no):")
print("Thanks for playing! See you next time 👋!")
                



        