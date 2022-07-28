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
        
        if word_user in 
    # 'Python'= {'P', 'y', 't','h', 'o', 'n'}