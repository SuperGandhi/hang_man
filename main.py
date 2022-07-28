import random
import string 

from words import words
from hangman_diagramns import lifes_dictionary_visual

def get_word_valided(words):
    """
        Select a word random to the list
        words valided
    """
    word = random.choice(words)
    
    while '-' in word or '' in word:
        word = random.choice(words)
    
    return word.upper()

def hang_man():
    print("-------------------------------------")
    print(" !Welcome to game the HANGMAN! ")
    print("-------------------------------------")
    
    word = get_word_valided(words)
    
    words_to_guess = set(word)
    guessed_letters = set()
    alphabet = set(string.ascii_uppercase)
    
    lifes = 7
    
    while len(words_to_guess) > 0 and lifes > 0:
        print(f"You have lives {lifes} left and you used these letters: {' '.join(guessed_letters)}")

        # Show the current state of the word
        word_list = [lyric if lyric in guessed_letters
                     else '-' for lyric in word]
        print(lifes_dictionary_visual[lifes])
        # Show the letters separated to space
        print(f"Word:{' '.join(word_list)}")
        
        word_user = input("Choose the word: ").upper()
    """
        if the word chosen by the user is in the alphabet and is not in the set of letters that have been entered, 
        the letter is added to the set of letters entered
    """
        
    if word_user in alphabet - guessed_letters:
        guessed_letters.add(word_user)
    # 'Python'= {'P', 'y', 't','h', 'o', 'n'}
    
    # If the letter is in the word
        if word_user in guessed_letters:
            guessed_letters.remove(word_user)
            print('')
        else:
            lifes = lifes - 1
            print(f"\nYou letter, {word_user} it's not your word.")
    # If the letter chosen of the user was already entered

    elif word_user in guessed_letters:
        print("\nYou already picked that letter. Please choose a new letter.")
    else:
        print("\nThis letter is not valid.")

    """
    The game reaches this line when all the letters of the word 
    are guessed or when the player's lives are exhausted.
    """
    if lifes == 0:
        print(lifes_dictionary_visual[lifes])
        print(f"!Hanged¡ you lost. So sorry. The word was: {word} ")
    else:
        print(f"!Excellent¡ you guessed the word {word}")

if __name__ == '__main__':    
    hang_man()