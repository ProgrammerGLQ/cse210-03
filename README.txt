Title: Jumper Game

Description : Jumper is a game in which the player seeks to solve a puzzle by guessing the 
letters of a secret word one at a time.


Project Structure

The main file imports from the Game class. In the main.py, the object  Game is instantiated which is invoked with the calling of class start_game(). The start_game() function is a public modifier and prints the welcome name as well as calls other relevant functions and classes in the game.py file.. The different files do the following:
The main class runs the Code, it invokes start_game() from game.py
The game.py file imports Player from player.py and imports Puzzle from puzzle.py. The Game calls the Player class and the Puzzle class
The game class starts the game
The player.py file imports Parachute from parachute.py. The player class calls Parachute
The player class saves the player´s name
The Puzzle.py file import random and the Puzzle class select and returns a secret word from a list
The Parachute class save the drawing of the man in parachute and erase the parachute lines

Required Software: Terminal, Any IDE 

Team member name            | Email address
Nelson Muchonji Bifwoli       bif20001@byui.edu 
Guillermo Quinteros           qui22003@byui.edu
Erika Ramirez                 ramirezerika328@gmail.com
Daniel                        das22001@byui.edu
