import csv
import random



def load_data(filename):
    """this function will loads the data and append it in a dictionary form like a key value pair"""
    kana_list=[]
    try:
        with open(filename,'r',encoding='utf-8')as file:
            reader=csv.DictReader(file)
            for row in reader:
                kana_list.append(row)
    except FileNotFoundError:
        print("❌ File not found. Make sure it's in the same folder as this script.")
        return []
    return kana_list

def quizuser(kana_list,level):
    score=0
    total=0
    mistake=0
    for item in kana_list:
        if mistake>=3:
            print("\n😓 You made 3 mistakes. Ending this level...")
            break

           
        print(f"\n whats is the romaji for {item["kana"]}")
        answer=input("Your answer:").strip().lower()
        correctanswer=item['Romaji'].strip().lower()
        total+=1
        if answer==correctanswer:
            print("Correct✅")
            score+=1
        else:
             print(f"Uh ohh! This answer is incorrect❌,The correct answer is {item['Romaji']}")
             mistake+=1
                
        
    if total == 0:
        percentage = 0
    else:
        percentage = (score / total) * 100
    return percentage>=90
    
def main():
    print("Yo!Welcome to Japanese Kana Flashcards😊.")
    choice=input("Choose one to learn:\n1.Hiragana\n  2.Katakana\n Enter 1 or 2:")
    if choice=="1":
        data = load_data('hiragana.csv')
    elif choice=="2":
        data = load_data('katakana.csv')
    else:
        print("Invalid choice")
        return
    for level in range(1,6):
        print(f"\n---Level{level}---")
        item_to_test=data[(level-1)*10:level*10]
        
        random.shuffle(item_to_test)
        passed=quizuser(item_to_test,level)
        if  not passed:
            print("You need atleast 90% Accuracy to unlock the next level. Try again😢💔!")
            break
        else:
            print("🎉 Level Passed❤️! Unlocking next level >>>")
    print("Thanks for Learning with me 🇯🇵")

print("Thanks for Learning with me ❤️")

# Program entry
response = input("Hey❤️! Do you want to start your Japanese journey? (yes/no): ").strip().lower()
if response == "yes":
    main()
else:
    print("No worries! Come back when you're ready. Sayonara❤️!")
