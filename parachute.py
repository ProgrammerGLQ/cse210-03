class Parachute:
    def __init__(self):
        self._lines = [
            ' ___ ',
            '/   \\',
            ' ___ ',
            '\\   /',
            ' \\ / ',
            '  0  ',
            ' /|\\',
            ' / \\ ',
            '      ',
            '^^^^^^^'
        ]
        self._is_spoilt = False
    def get_status(self):
        return self._is_spoilt
    def set_status(self, status):
        self._is_spoilt = status
    def show(self):
        for i in range(len(self._lines)):
            print(self._lines[i])
    def dent_parachute(self):
        if len(self._lines) == 5:
            self._lines[0] = '  X  '
            self._is_spoilt = True
        else:
            del self._lines[0]
            self._is_spoilt = False