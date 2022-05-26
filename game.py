from player import Player
from puzzle import Puzzle


def is_solved(secret_word):
    for letter in secret_word:
        if letter == '-':
            continue
        else:
            return False
    return True


class Game:
    def __init__(self):
        self._puzzle = Puzzle()
        self._player = Player()
        self._secret_word = self._puzzle.get_secret_word()
        self._reveal_box = self.setup_reveal_box()

    def get_player(self):
        return self._player

    def set_player(self, player):
        self._player = player

    def get_secret_word(self):
        return self._secret_word

    def set_secret_word(self, word):
        self._secret_word = word

    def get_reveal_box(self):
        return self._reveal_box

    def set_reveal_box(self, box):
        self._reveal_box = box

    def get_puzzle(self):
        return self._puzzle

    def set_puzzle(self, puzzle):
        self._puzzle = puzzle

    def start_game(self):
        print("\nWelcome to Jumper.")
        name = input('Hey, what is your name? ')
        self._player.set_name(name)
        self.make_guess()

    def make_guess(self):
        print(self.get_reveal_box())
        self._player.get_parachute().show()
        guess = input(self.get_player().get_name() + ', Guess a letter [a-z]: ').lower()
        if guess in self._secret_word:
            self.reveal_letter(guess)
            if is_solved(self._secret_word):
                print()
                print(self.get_player().get_name() + ' Won!\n')
            else:
                self.make_guess()
        else:
            self._player.get_parachute().dent_parachute()
            if self._player.get_parachute().get_status():
                self._player.get_parachute().show()
                print()
                print(self.get_player().get_name() + ' GAME OVER!!\n')
            else:
                self.make_guess()

    def reveal_letter(self, letter):
        word = list(self._secret_word)
        box = list(self._reveal_box)
        for i in range(len(word)):
            if word[i] == letter:
                box[i * 2] = letter
        self.set_reveal_box("".join(box))

        self.set_secret_word(self._secret_word.replace(letter, '-'))

    def setup_reveal_box(self):
        reveal_box = ''
        word_length = len(self._puzzle.get_secret_word())
        for i in range(word_length):
            reveal_box += '_ '

        return reveal_box
