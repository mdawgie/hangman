import random
import sys

def main():

    word_list = ["Hello","Keyboard","Rock","Paper","Scissors","Mouse", "Moniter","Computer","Python"]
    randomchoice = random.choice(word_list)
    lenth = len(randomchoice)
    print("The answer is a",lenth,"letter word.")
    lives = lenth
    guessed_letters = []
    while lives>0:
        
        print("You have",lenth,"lives remaining")
        guess = input("Guess a letter")
        guessed_letters.append(guess)
        if checkWin(guessed_letters, randomchoice):
            print("Correct,",guess)
        else:
            print("Incorrect")
            lives = lives - 1
                        
    if (lives == 0):
        print("You Lose")
    
            
                 

def checkWin(guessed_letters, selected_word):
    flag = False
    for letter in selected_word:
        if guessed_letters[-1] == letter:
            flag = True
     
    return flag
      

if __name__ == "__main__":
    main()
