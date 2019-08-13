import random
import sys

def main():

    word_list = ["Hello","Keyboard","Rock","Paper","Scissors","Mouse", "Moniter","Computer","Python"]
    randomchoice = random.choice(word_list)
    lenth = len(randomchoice)
    print("The answer is a",lenth,"letter word. You have",lenth,"lives remaining")
    input("Guess a letter")
    
def checkWin(guessed_letters, selected_word):
    pass
    

if __name__ == "__main__":
    main()