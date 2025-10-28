import pygame as pg

from src.assets.definitions import alpha_keymap

from src.button import NavButtonManager
from src.word_manager import WordManager

from src.board import Board
from src.keyboard import Keyboard

from src.commands import AddLetterCommand
from src.commands import RemoveLetterCommand
from src.commands import ValidateWordCommand
from src.commands import QuitGameCommand
from src.commands import NewGameCommand

from src.event_handler import GameKeypadMouseUpHandler
from src.event_handler import GameKeypadBackspaceHandler
from src.event_handler import GameKeypadReturnHandler

from src.event_handler import KeyboardKeyPressHandler
from src.event_handler import GameKeypadMouseMotionHandler
from src.event_handler import KeyboardReturnHandler
from src.event_handler import KeyboardBackspaceHandler

from src.event_handler import NavButtonMouseOverHandler
from src.event_handler import NavButtonMouseUpHandler

from src.state import InitialGameState
from src.state import PlayGameState

__all__ = ["StateManager"]


#---------------------------------------------------------------------------------------------------
#   State Manager
#
class StateManager:
    # -------------------------------------------------------------------------------------------------
    #
    #
    states = {
        "Initial": InitialGameState(),
        "Play": PlayGameState(),
    }

    transition_rules = {
        "Initial": ["Play"],
        "Play": ["Start", "Quit"],
        "Start": ["New", "Quit"],
        "New": ["Start", "Quit"]
    }

    # -------------------------------------------------------------------------------------------------
    #
    #
    def __init__(self, canvas, event_manager):
        self.cur_state = None

        self.canvas = canvas
        self.event_manager = event_manager

        self.tiles = Board()
        self.keyboard = Keyboard()
        self.nav_button_manager = NavButtonManager()
        self.word_manager = WordManager(self.tiles, self.keyboard)

        self.add_letter_command = AddLetterCommand(self.word_manager)
        self.remove_letter_command = RemoveLetterCommand(self.word_manager)
        self.validate_word_command = ValidateWordCommand(self.word_manager)
        self.quit_game_command = QuitGameCommand()
        self.new_game_command = NewGameCommand(
            [
                self.tiles,
                self.keyboard,
                self.word_manager
            ]
        )

    # -------------------------------------------------------------------------------------------------
    #   Set Initial State
    #
    def set_initial_state(self, initial_state: str):
        if initial_state in self.states:
            self.transition_to(initial_state)

    # -------------------------------------------------------------------------------------------------
    #   Transition To
    #
    def transition_to(self, state: str):
        #
        #   This "if" handles the first call to transition_to from set_initial_state
        #
        if not self.cur_state:
            self.cur_state = self.states[state]

        elif state in self.states and state in self.transition_rules[self.cur_state.name]:
            self.cur_state = self.states[state]

        self.handle_state_specific_actions(state)

    # -------------------------------------------------------------------------------------------------
    #   Handle State Specific Actions
    #
    def handle_state_specific_actions(self, state: str):
        if state == "Initial":
            self.event_manager.subscribe(pg.MOUSEBUTTONUP, NavButtonMouseUpHandler(self))
            self.event_manager.subscribe(pg.MOUSEMOTION, NavButtonMouseOverHandler(self))

        if state == "Play":
            self.tiles.build()
            self.keyboard.build()

        elif state == "Start":
            self.word_manager.set_wordle_word()
            # -------------------------------------------------------------------------------------
            #   Initialize Keyboard Command Handlers
            #
            keyboard_keypress_handler = KeyboardKeyPressHandler(self.add_letter_command)
            keyboard_return_handler = KeyboardReturnHandler(self.validate_word_command)
            keyboard_backspace_handler = KeyboardBackspaceHandler(self.remove_letter_command)

            # -------------------------------------------------------------------------------------
            #   Initialize Keypad Command Handlers
            #
            game_keypad_motion_handler = GameKeypadMouseMotionHandler(self.keyboard)

            game_keypad_mouseup_handler = GameKeypadMouseUpHandler(
                self.keyboard,
                self.add_letter_command
            )

            game_keypad_return_handler = GameKeypadReturnHandler(
                self.keyboard,
                self.validate_word_command
            )

            game_keypad_backspace_handler = GameKeypadBackspaceHandler(
                self.keyboard,
                self.remove_letter_command
            )

            # -------------------------------------------------------------------------------------
            #   Subscriptions
            #
            # -------------------------------------------------------------------------------------
            #   Sub all keys from A - Z
            #
            for event in alpha_keymap.values():
                self.event_manager.subscribe(event, keyboard_keypress_handler)
            # -------------------------------------------------------------------------------------
            #   Keyboard specific handlers
            #
            self.event_manager.subscribe(pg.KEYDOWN, keyboard_keypress_handler)
            self.event_manager.subscribe(pg.K_RETURN, keyboard_return_handler)
            self.event_manager.subscribe(pg.K_BACKSPACE, keyboard_backspace_handler)
            # -------------------------------------------------------------------------------------
            #   Keypad specific handlers
            #
            self.event_manager.subscribe(pg.MOUSEMOTION, game_keypad_motion_handler)
            self.event_manager.subscribe(pg.MOUSEBUTTONUP, game_keypad_mouseup_handler)
            self.event_manager.subscribe(pg.MOUSEBUTTONUP, game_keypad_return_handler)
            self.event_manager.subscribe(pg.MOUSEBUTTONUP, game_keypad_backspace_handler)


        elif state == "New":
            self.new_game_command.execute()

        elif state == "Quit":
            self.quit_game_command.execute()

        else:
            pass
