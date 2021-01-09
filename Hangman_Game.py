#************************
#
#       HANGMAN GAME
#                       ersinkaanaygun
#
#************************

# 1) import the random library
import random
# 2) read and store all the list of words from scrabble-words.txt
word_list = open("scrabble-words.txt").readlines()
# 3) generate and store a random word within the list
def get_word():
    word = random.choice(word_list)
    return word.upper()  
# greet the user and ask if they want to play. If no quit the game
def Initial_Validation():
    print("\n")
    print("*"*50)
    print("*")
    print("*",""*30,"Welcome to HANGMAN",""*30)
    print("*")
    print("*"*50)
    while True:
        startornot = str(input('Would you like to play? (Y/N)\t'))
        if (startornot.lower() == "y"):
            return True
        elif (startornot.lower() == "n"):
            return False
        else:
            print('\nInvalid answer, please try again\n')
            continue
   
# if yes, ask and store the value of the total amount of chances the user would like to guess the word
# ask for a letter
# Based on the letter the user entered show whether:
    # the user won or lost the game and in both cases display the selected word  
    # if they haven't won or lost show the following:
        #  a random word but replace each unguessed letter with an underscore _ 
            # (add a blank next to each underscore to show how many letters there are in the word)
        #  set of incorrectly and correctly guessed letters 
        # alerting the user how many guesses they have remaining
        # Example:
            # You have correctly guessed these letters: F _ _ _ F _ _ L D
            # You have already guessed these letters [Q, Z, F, D, P, L]
            # You have (X) guesses remaining. X = "the number of guesses left"
#  continue playing until the user has run out of quesses
def lets_play(word):
    word_underscore = "_" * (len(word)-1)
    print(word_underscore)
    print("The word contains ", len(word) -1 ,"letters")
    guessed = False
    guessed_letters = []
    guessed_words = []
    print("You can either enter number of chances according to difficulties or any amount of changes;")
    print("\tHARD:\t4")
    print("\tMEDIUM:\t6")
    print("\tEASY:\t8")
    number_of_tries = int(input("Please enter total amount of chances:\t"))
    print("Let's play some fun game, are you ready? Here we go!")  
    print("You have ",number_of_tries," chances to guess the word, good luck!")
    print("\n")
    
    while not guessed and number_of_tries > 0:
        guess = input("Please guess a letter or word:  ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter",guess)
            elif guess not in word:
                print(guess," is not in the word.")
                number_of_tries -= 1
                guessed_letters.append(guess)
            else:
                print(guess," is in the  word, nice job!")
                guessed_letters.append(guess)
                list_word = list(word_underscore)
                change_underscores = [i for i, letter in enumerate(word) if letter == guess]
                for x in change_underscores:
                    list_word[x] = guess
                word_underscore="".join(list_word)
                if "_" not in word_underscore:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed ", guess)
            elif guess != word:
                print("boops! ",guess," is not the word")
                number_of_tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_underscore = word
        else:
            print("Not a valid guess")
        print(word_underscore)
        print("\n")
        print(guessed_letters)
        print("You have ",number_of_tries," guesses remaining")
    if guessed:
        print("YOU WIN!")
    else:
        print("Sorry Champ! you ran out of tries. The word was\t",word)

# after the game is over ask if they would like to play again
def again():
    while True:
        startornot = Initial_Validation()
        if startornot == False:
            break
        word = get_word()
        lets_play(word)
        while input ("Would you like to play again? (Y/N)\t").upper() == "Y":
            word =get_word()
            lets_play(word)
        
if __name__ == "__main__":
    again()