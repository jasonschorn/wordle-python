from abc import ABC, abstractmethod
from enum import IntEnum
import src.assets.definitions as df

__all__ = [
    "NavButtonMouseOverHandler",
    "NavButtonMouseUpHandler",
    "GameKeypadMouseUpHandler",
    "GameKeypadMouseMotionHandler",
    "GameKeypadReturnHandler",
    "GameKeypadBackspaceHandler",
    "KeyboardKeyPressHandler",
    "KeyboardReturnHandler",
    "KeyboardBackspaceHandler",
]


# -------------------------------------------------------------------------------------------------
#   Index Reference
#
class Index(IntEnum):
    """
        For ease of determining the type of object that is being accessed
    """
    MousePos = 0
    ButtonName = 0


# -------------------------------------------------------------------------------------------------
#   HANDLER BASE CLASS
#
class Handler(ABC):
    """
        Handlers take input from event listeners and delegate responsibility
    """
    @abstractmethod
    def handle_it(self, *args):
        pass


# -------------------------------------------------------------------------------------------------
#
# --> NAV BUTTON HANDLERS
#
# -------------------------------------------------------------------------------------------------
#   NAV BUTTON MOUSE OVER HANDLER
# -------------------------------------------------------------------------------------------------
class NavButtonMouseOverHandler(Handler):
    def __init__(self, state_manager):
        self.state_manager = state_manager

    def handle_it(self, *args):
        self.state_manager.cur_state.handle_mouse_over(args[Index.MousePos])


# -------------------------------------------------------------------------------------------------
#   NAV BUTTON MOUSE UP HANDLER
#
class NavButtonMouseUpHandler(Handler):
    def __init__(self, state_manager):
        self.state_manager = state_manager

    def handle_it(self, *args):
        for button in self.state_manager.cur_state.buttons:
            if button.button_rectangle.collidepoint(args[Index.MousePos]):
                self.state_manager.transition_to(button.label)


# -------------------------------------------------------------------------------------------------
#
# --> GAME KEYPAD HANDLERS
#
# -------------------------------------------------------------------------------------------------
#  Keyboard Mouse Up Handler
#
class GameKeypadMouseUpHandler(Handler):
    def __init__(self, keyboard, add_letter_command):
        self.keyboard = keyboard
        self.add_letter_command = add_letter_command

    # ---------------------------------------------------------------------------------------------
    #
    def handle_it(self, *args):
        #
        #   Command --> WordManager.add_letter
        #
        for key in self.keyboard.keypad:
            if key.rectangle.collidepoint(args[Index.MousePos]):
                self.add_letter_command.execute(
                    self.keyboard.get_letter(
                        self.keyboard.keypad.index(key)
                    )
                )


# -------------------------------------------------------------------------------------------------
#   KEYPAD MOUSE MOTION HANDLER
#
class GameKeypadMouseMotionHandler(Handler):
    def __init__(self, keyboard):
        self.keyboard = keyboard

    # ---------------------------------------------------------------------------------------------
    #
    def handle_it(self, *args):
        """
            Iterate over keyboard buttons checking for collision and, while a collision
            exists, change the buttons background color

                *args = current mouse pos
        """
        for key in self.keyboard.keypad:
            if key.rectangle.collidepoint(args[Index.MousePos]):
                key.color = df.ButtonMouseOverColor
            else:
                self.keyboard.update_key(key)


# -------------------------------------------------------------------------------------------------
#   KEYPAD RETURN HANDLER
#
class GameKeypadReturnHandler(Handler):
    def __init__(self, keyboard, command):
        self.keyboard = keyboard
        self.validate_word_command = command

    # ---------------------------------------------------------------------------------------------
    #
    def handle_it(self, *args):
        for key in self.keyboard.keypad:
            if key.rectangle.collidepoint(args[Index.MousePos]):
                if self.keyboard.letters[key.index].label == "Return":
                    self.validate_word_command.execute(*args)


# -------------------------------------------------------------------------------------------------
#   KEYPAD BACKSPACE HANDLER
#
class GameKeypadBackspaceHandler(Handler):
    def __init__(self, keyboard, command):
        self.keyboard = keyboard
        self.backspace_command = command

    #----------------------------------------------------------------------------------------------
    #
    def handle_it(self, *args):
        for key in self.keyboard.keypad:
            if key.rectangle.collidepoint(args[Index.MousePos]):
                if self.keyboard.letters[key.index].label == "Delete":
                    self.backspace_command.execute(*args)


# -------------------------------------------------------------------------------------------------
#
# --> KEYBOARD HANDLERS
#
# -------------------------------------------------------------------------------------------------
#   KEYBOARD KEY PRESS HANDLER
# -------------------------------------------------------------------------------------------------
class KeyboardKeyPressHandler(Handler):
    def __init__(self, command):
        self.command = command

    # ---------------------------------------------------------------------------------------------
    #
    def handle_it(self, key_pressed):
        """
            Command --> WordManager.add_letter
        """
        if key_pressed in df.alphabet:
            self.command.execute(key_pressed.upper())


# -------------------------------------------------------------------------------------------------
#   KEYBOARD RETURN HANDLER
#
class KeyboardReturnHandler(Handler):
    def __init__(self, command):
        self.validate_word_command = command

    # ---------------------------------------------------------------------------------------------
    #
    def handle_it(self, *args):
        """
            command --> WordManager.validate
        """
        self.validate_word_command.execute(*args)


# -------------------------------------------------------------------------------------------------
#   KEYBOARD BACKSPACE HANDLER
#
class KeyboardBackspaceHandler(Handler):
    def __init__(self, command):
        self.backspace_command = command

    # ---------------------------------------------------------------------------------------------
    #
    def handle_it(self, *args):
        self.backspace_command.execute(*args)
