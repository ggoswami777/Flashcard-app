import random

def play():
    user_score=0
    computer_score=0
    options=["r","p","s"]
    print("Welcome to Rock-Paper-Scissors!\nFirst to 3 points wins the game.\n")
    while user_score<3 and computer_score<3:
        user=input(" What is your choice?\n'r' for rock 🪨 ,'p' for paper 📄 , 's' for scissors ✂️\n").lower()
        if user not in options:
            print("Invalid input.Please enter 'r', 'p', 's'.\n")
            continue
        computer=random.choice(options)
        print(f"\nYou chose 🙋‍♂️  {user}, computer🤖 chose {computer}.")

        if user==computer:
            print("It is a tie 🤝")
        
        elif iswin(user,computer):
            user_score+=1
            print("You Won this round 🏆!")
        else:
            computer_score+=1
            print("You lost")
        print(f"Score => You: {user_score} | Computer:{computer_score}\n")
    if user_score == 3:
        print("Congratulations! 🎉 You won the game!")
    else:
        print("Game over 💥! Computer wins. Better luck next time!")
    play_again = input("\nDo you want to play again? (y/n): ").lower()
    if play_again == 'y':
        play()  
    else:
        print("Thanks for playing! 👋") 

        
def iswin(player,opponent):
    #return true if player wins
    #r>s,s>p,p>r
    if(player=="r" and opponent=="s") or (player=="s" and opponent=="p") or (player=="p" and opponent=="r"):
        return True

#running code

play()
