# -------------------------------------------------------------------------------------------------
#   State
#
#
#
from abc import ABC, abstractmethod
from copy import deepcopy
from enum import IntEnum
import pygame as pg

from src.assets.templates import splash_logo_template
from src.assets.templates import splash_logo_shadow_template
from src.assets.templates import game_button_template
from src.button import Button
from src.event_handler import NavButtonMouseOverHandler
from src.event_handler import NavButtonMouseUpHandler
from src.text import TextBuilder

import src.assets.definitions as df

__all__ = ["InitialGameState", "PlayGameState"]


# -------------------------------------------------------------------------------------------------
#   Enums for readability
#
class RenderArgs(IntEnum):
    Canvas = 0
    StateManager = 1


class Index(IntEnum):
    MousePos = 0
    StateManager = 1
    xCoord = 0
    yCoord = 1


# -------------------------------------------------------------------------------------------------
#   State Abstract Base Class
#
class State(ABC):

    @abstractmethod
    def render(self, *args, **kwargs):
        pass

    @abstractmethod
    def handle_mouse_over(self, *args, **kwargs):
        pass

    @abstractmethod
    def check_for_mouse_up_event(self, *args, **kwargs):
        pass

    @abstractmethod
    def handle_subscriptions(self, *args, **kwargs):
        pass


# -------------------------------------------------------------------------------------------------
#   Initial Game State
#
class InitialGameState(State):
    # -------------------------------------------------------------------------------------------------
    #
    #
    button_names = ["Play"]

    button_coords = [
        (df.PlayButtonX, df.PlayButtonY),
    ]

    # -------------------------------------------------------------------------------------------------
    #
    #
    def __init__(self):
        self.name = "Initial"
        self.buttons = self.initialize_buttons()
        self.splash_logo = self.build_splash_logo()
        self.splash_logo_shadow = self.build_splash_shadow_logo()

    # ---------------------------------------------------------------------------------------------
    #   Initialize Buttons
    #
    def initialize_buttons(self):
        buttons = []

        for index, label in enumerate(self.button_names):
            button = Button()
            button_template = deepcopy(game_button_template)
            button_template['x'] = self.button_coords[index][Index.xCoord]
            button_template['y'] = self.button_coords[index][Index.yCoord]
            button_template['label'] = label
            button.build(button_template)

            buttons.append(button)

        return buttons

    # ---------------------------------------------------------------------------------------------
    #   Splash Logo
    #
    @staticmethod
    def build_splash_logo():
        tb = TextBuilder()
        return tb.build(splash_logo_template)

    # ---------------------------------------------------------------------------------------------
    #   Shadow for Splash Logo
    #
    @staticmethod
    def build_splash_shadow_logo():
        tb = TextBuilder()
        return tb.build(splash_logo_shadow_template)

    # -------------------------------------------------------------------------------------------------
    #   Mouse Over Event Handler
    #
    def handle_mouse_over(self, *args, **kwargs):
        for button in self.buttons:
            if button.button_rectangle.collidepoint(args[Index.MousePos]):
                button.button_color = df.ButtonMouseOverColor
            else:
                button.button_color = df.ButtonBgColor

    # -------------------------------------------------------------------------------------------------
    #   Mouse Up Event Handler
    #
    def check_for_mouse_up_event(self, *args, **kwargs):
        for button in self.buttons:
            if button.button_rectangle.collidepoint(args[Index.MousePos]):
                args[Index.StateManager].transition_to(button.label)

    # -------------------------------------------------------------------------------------------------
    #   Event Subscription Handler
    #
    def handle_subscriptions(self, state_manager):
        state_manager.event_manager.subscribe(
            pg.MOUSEMOTION,
            NavButtonMouseOverHandler(state_manager)
        )
        state_manager.event_manager.subscribe(
            pg.MOUSEBUTTONUP,
            NavButtonMouseUpHandler(state_manager)
        )

    # -------------------------------------------------------------------------------------------------
    #   Render all State Assets
    #
    def render(self, *args):
        canvas = args[RenderArgs.Canvas]
        self.splash_logo.rectangle.center = (df.SplashX, df.SplashY)
        self.splash_logo_shadow.rectangle.center = (df.SplashX + 3, df.SplashY + 5)

        for button in self.buttons:
            button.draw(canvas)

        canvas.blit(
            self.splash_logo_shadow.renderable_text_object,
            self.splash_logo_shadow.rectangle
        )
        canvas.blit(
            self.splash_logo.renderable_text_object,
            self.splash_logo.rectangle
        )


# -------------------------------------------------------------------------------------------------
#   Play Game State
#
class PlayGameState(State):
    # ---------------------------------------------------------------------------------------------
    #   State Specific Navigation Buttons
    #
    button_names = ["Start", "New", "Quit"]

    buttons_coords = [
        (df.StartButtonX, df.StartButtonY),
        (df.NewButtonX, df.NewButtonY),
        (df.QuitButtonX, df.QuitButtonY)
    ]

    # ---------------------------------------------------------------------------------------------
    #
    #
    def __init__(self):
        self.name = "Play"
        self.buttons = self.initialize_buttons()

    # ---------------------------------------------------------------------------------------------
    #   Initialize Buttons
    #
    def initialize_buttons(self):
        buttons = []

        for index, label in enumerate(self.button_names):
            button = Button()
            button_template = deepcopy(game_button_template)
            button_template['x'] = self.buttons_coords[index][Index.xCoord]
            button_template['y'] = self.buttons_coords[index][Index.yCoord]
            button_template['label'] = label
            button.build(button_template)

            buttons.append(button)

        return buttons

    # -------------------------------------------------------------------------------------------------
    #   Mouse Over Event Handler
    #
    def handle_mouse_over(self, *args, **kwargs):
        for button in self.buttons:
            if button.button_rectangle.collidepoint(args[Index.MousePos]):
                button.button_color = df.ButtonMouseOverColor
            else:
                button.button_color = df.ButtonBgColor

    # ---------------------------------------------------------------------------------------------
    #   Mouse Up Event Handler
    #
    def check_for_mouse_up_event(self, *args, **kwargs):
        for button in self.buttons:
            if button.button_rectangle.collidepoint(args[Index.MousePos]):
                args[Index.StateManager].transition_to(button.label)

    # -------------------------------------------------------------------------------------------------
    #   Event Subscription Handler
    #
    def handle_subscriptions(self, state_manager):
        pass

    # ---------------------------------------------------------------------------------------------
    #   Render all State Assets
    #
    def render(self, *args):
        """
        Render requires: (1) canvas to draw on, (2) reference to the game tiles, (3) reference to
        the keyboard tiles, (4) reference to the word manager that controls the inputted letters
        as well as the words.
        """
        # -----------------------------------------------------------------------------------------
        #   References to external classes
        #
        canvas = args[RenderArgs.Canvas]
        board = args[RenderArgs.StateManager].tiles
        keyboard = args[RenderArgs.StateManager].keyboard
        word_manager = args[RenderArgs.StateManager].word_manager
        # -----------------------------------------------------------------------------------------
        #   Render State Specific Buttons
        #
        for button in self.buttons:
            button.draw(canvas)
        # -----------------------------------------------------------------------------------------
        #   Draw the Wordle game board
        #
        for rectangle in board.tiles:
            pg.draw.rect(
                canvas,
                rectangle.color,
                rectangle.rectangle,
                rectangle.thickness
            )
        # -----------------------------------------------------------------------------------------
        #   Draw colored tiles on the Wordle game board after each guess
        #
        if board.guess_tiles:
            for tile in board.guess_tiles:
                pg.draw.rect(
                    canvas,
                    tile.color,
                    tile.rectangle,
                    tile.thickness
                )
        # ------------------------------------------------------------------------------------------
        #   Draw letters on Wordle board
        #
        for index, letter in enumerate(word_manager.renderable_letters):
            letter.rectangle.center = board.tiles[index].rectangle.center

            canvas.blit(letter.renderable_text_object, letter.rectangle)
        # ------------------------------------------------------------------------------------------
        #   Render Game Keypad
        #
        for key in keyboard.keypad:
            pg.draw.rect(
                canvas,
                key.color,
                key.rectangle,
                key.thickness,
                key.curve
            )
        #------------------------------------------------------------------------------------------
        #   Add Letters to the Keypad
        #
        for index, letter in enumerate(keyboard.letters):
            if index < df.AlphabetLength:
                letter.rectangle.center = keyboard.keypad[index].rectangle.center

                canvas.blit(
                    letter.renderable_text_object,
                    letter.rectangle
                )
            else:
                # ---------------------------------------------------------------------------------
                #   Add Return Key
                #
                keyboard.letters[df.ReturnKeyIndex].rectangle.center = keyboard.keypad[
                    df.ReturnKeyIndex].rectangle.center
                canvas.blit(
                    keyboard.letters[df.ReturnKeyIndex].renderable_text_object,
                    keyboard.letters[df.ReturnKeyIndex].rectangle
                )
                # ---------------------------------------------------------------------------------
                #   Add Backspace Key
                #
                keyboard.letters[df.BackspaceKeyIndex].rectangle.center = keyboard.keypad[
                    df.BackspaceKeyIndex].rectangle.center
                canvas.blit(
                    keyboard.letters[df.BackspaceKeyIndex].renderable_text_object,
                    keyboard.letters[df.BackspaceKeyIndex].rectangle
                )


# ---------------------------------------------------------------------------------------------------
#
#   NOT USED
#
# ---------------------------------------------------------------------------------------------------
#
#
class StartGameState(State):
    def __init__(self):
        self.name = "Start"

    def handle_mouse_over(self, *args, **kwargs):
        pass

    def check_for_mouse_up_event(self, *args, **kwargs):
        pass

    def handle_subscriptions(self, state_manager):
        pass

    def render(self, *args):
        pass


# ---------------------------------------------------------------------------------------------------
#
#
class NewGameState(State):
    def __init__(self):
        self.name = "New"

    def handle_mouse_over(self, *args, **kwargs):
        pass

    def check_for_mouse_up_event(self, *args, **kwargs):
        pass

    def handle_subscriptions(self, state_manager):
        pass

    def render(self, *args):
        pass


# ---------------------------------------------------------------------------------------------------
#
#
class QuitGameState(State):
    def __init__(self):
        self.name = "Quit"

    def handle_mouse_over(self, *args, **kwargs):
        pass

    def check_for_mouse_up_event(self, *args, **kwargs):
        pass

    def handle_subscriptions(self, state_manager):
        pass

    def render(self, *args):
        pass
