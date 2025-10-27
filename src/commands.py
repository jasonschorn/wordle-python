# -------------------------------------------------------------------------------------------------
#   Command
#
from abc import ABC
from enum import IntEnum
from sys import exit

import pygame as pg


# -------------------------------------------------------------------------------------------------
#
#
class Index(IntEnum):
    BoardPos = 0
    PrintLetter = 1
    Letter = 0
    Flags = 0


# -------------------------------------------------------------------------------------------------
#   Abstract Base Command Class
#
class Command(ABC):

    def execute(self, *args):
        pass


# -------------------------------------------------------------------------------------------------
#   Add Letter Command
#
class AddLetterCommand(Command):
    """
        Command to Word Manager and adds a letter to the Wordle board based on user input
            - Physical keyboard
            - Game keypad buttons
    """

    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self, *args):
        self.receiver.add_letter(*args)


# -------------------------------------------------------------------------------------------------
#   Remove Letter Command
#
class RemoveLetterCommand(Command):
    """
        Command to Word Manager and removes a letter from the Wordle board provided there
        are letters on the board
    """

    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self, *args):
        self.receiver.remove_letter()


# -------------------------------------------------------------------------------------------------
#   Validate Word Command
#
class ValidateWordCommand(Command):
    """
        Command to Word Manager to validate input after the Return key is pressed
    """

    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self, *args):
        self.receiver.validate()


# -------------------------------------------------------------------------------------------------
#   Create Renderable Letter
#
class CreateRenderableLetter(Command):
    """
    Command to create a letter from user input that will be rendered to the Wordle board

        Index.BoardPos is from Word Manager renderIndex
        Index.PrintLetter is the current letter entered by the user
    """

    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self, *args):
        self.receiver.create_renderable_letter(args[Index.BoardPos], args[Index.PrintLetter])


# -------------------------------------------------------------------------------------------------
#   Update Board After Return
#
class UpdateBoardAfterReturn(Command):
    """
    Command to the Board Class to update the Wordle board after the return key/button is pressed.
    Renders a colored tile to the Wordle board based on the validity of the input.
    """

    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self, *args):
        self.receiver.update_board(args[Index.Flags])


# -------------------------------------------------------------------------------------------------
#   Set Flags and Letters
#
class SetFlagsAndLetters(Command):
    """
    Command to Word Manager Class that is used by UpdateKeypadAfterReturn to maintain a reference
    to the color state that keys must maintain after each time the return key/buttons is pressed
    """

    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self, *args):
        self.receiver.set_flags_and_letters(*args)


# -------------------------------------------------------------------------------------------------
#   Update Keypad After Return
#
class UpdateKeypadAfterReturn(Command):
    """
        Command to Word Manager that updates the background color on the keypad
    """

    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self, *args):
        self.receiver.update_keypad(*args)


# -------------------------------------------------------------------------------------------------
#   New Game Command
#
class NewGameCommand(Command):
    """
        Command to Board, Keyboard, and Word Manager to reset/clear
        current game state
    """

    # TODO --> Consider removing init and passing list of receivers to execute
    #
    def __init__(self, receivers: list):
        self.receivers = receivers

    def execute(self, *args):
        for receiver in self.receivers:
            receiver.new_game()


# -------------------------------------------------------------------------------------------------
#   Quit Game Command
#
class QuitGameCommand(Command):
    def execute(self, *args):
        pg.quit()
        exit()


# -------------------------------------------------------------------------------------------------
#   Not Used
#
class StartGame(Command):
    """
        Receiver --> StateManager
    """

    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self, *args):
        self.receiver.transition(self.receiver.states["Play"])
