import random
import sys

def main():

    word_list = ["Hello","Keyboard","Rock","Paper","Scissors","Mouse", "Moniter","Computer","Python"]
    randomchoice = random.choice(word_list)
    lenth = len(randomchoice)
    print("The answer is a",lenth,"letter word. You have",lenth,"lives remaining")
    guess = input("Guess a letter")
    for letter in randomchoice:
        if guess == letter:
            
        print("Correct")
    
def checkWin(guessed_letters, selected_word):
    pass
    

if __name__ == "__main__":
    main()
