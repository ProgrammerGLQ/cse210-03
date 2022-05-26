import random

class Puzzle:
    def __init__(self):

        self._words = ['apple', 'act','action','activity','actor','actually', 'advice', 'agree', 'cars', 'cat', 'cook', 
        'bored', 'button', 'bee', 'calm', 'cold', 'dinner', 'dust', 'divide', 'easy', 'dinosaurs',
        'food', 'error', 'fun', 'earth', 'eyes', 'familiar', 'fade', 'faith', 'fall', 'movies',
        'dog', 'water', 'mountain', 'mother', 'father', 'milk', 'cereal', 'meat', 'food', 'music',
        'colors', 'ocean', 'share', 'wash', 'tired', 'restroom', 'weather', 'welcome', 'week',
        'watch', 'television', 'sun', 'wonderful', 'zebra', 'zipper', 'zoo', 'time', 'team', 'data', 'animal', 'tree', 'space', 'universe', 'follow', 
        'movie', 'kitchen', 'park', 'pen', 'phone', 'computer']

        self._secret_word = random.choice(self._words)

    def get_words(self):
        return self._words

    def set_words(self, words):
        self._words = words

    def get_secret_word(self):
        return self._secret_word