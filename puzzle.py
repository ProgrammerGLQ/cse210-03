import random
import string

words = ('apple', 'act','action','activity','actor','actually', 'advice', 'agree', 'cars', 'cat', 'cook', 
'bored', 'button', 'bee', 'calm', 'cold', 'dinner', 'dust', 'divide', 'easy', 'dinosaurs',
'food', 'error', 'fun', 'earth', 'eyes', 'familiar', 'fade', 'faith', 'fall', 'movies',
'dog', 'water', 'mountain', 'mother', 'father', 'milk', 'cereal', 'meat', 'food', 'music',
'colors', 'ocean', 'share', 'wash', 'tired', 'restroom', 'weather', 'welcome', 'week',
'watch', 'television', 'sun', 'wonderful', 'zebra', 'zipper', 'zoo', 'time')

lives = 14

def get_words(words):
    word = random.choice(words)
    while '_' in word or ' ' in word:
        word = random.choice(words)
    return words

def puzzle():
    word = get_words(words)
    #keeping track of what the users letter they used
    word_letters = set(word)
    alphabet = set(string.ascii_lowercase)
    user_used_letters = set()

    while len(word_letters) > 0 and lives > 0:
        print('You only', lives, 'left. This letters you have used: ', ' '.join(user_used_letters))
        word_list = [letter if letter in user_used_letters 
            else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Please, guess a letter (a-z): ').lower()
        if user_letter in alphabet - user_used_letters:
            user_used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            #when user inputs the wrong letter
            else:
                lives = lives - 1 
                print('Letter is not part of the word.')
        elif user_letter in user_used_letters:
            print('Sorry, you already choose this letter. ')
        else:
            print('Please, input a valid letter. ')
    
    if lives == 0:
        print('Sorry you have no more parachute. GAME OVER. The word was', word)
    else:
        print('You solved the puzzle', word)

puzzle()