from parachute import Parachute
class Player:
    def __init__(self):
        self._name = 'player1'
        self._parachute = Parachute()
    def get_name(self):
        return self._name
    def set_name(self, name):
        self._name = name
    def get_parachute(self):
        return self._parachute
    def set_parachute(self, parachute):
        self._parachute = parachute