from copy import deepcopy
from enum import IntEnum

from src.rectangle import Rectangle, RectangleBuilder
from src.text import Text, TextBuilder

import src.assets.definitions as df
import src.assets.templates as tpl

# -------------------------------------------------------------------------------------------------
#
#
__all__ = ["Keyboard"]


# -------------------------------------------------------------------------------------------------
#
#
class Index(IntEnum):
    Flags = 0
    Letters = 1


# -------------------------------------------------------------------------------------------------
#   Keyboard
#
class Keyboard:
    """
    The Keyboard class consists of a collection of (1) rectangles
    that represent a hybrid keyboard keypad; (2) the letters of
    the keypad as well as the return and backspace keys; (3) a
    collection of letters that the player has chosen; (4) a set
    of flags used to determine a given keys background color.

    The collection of chosen letters is in one-to-one
    correspondence with the flags.  That is, whenever return is
    pressed, the set of chosen letters are validated and
    subsequently assigned one of three possible flags.
        1- Invalid Chosen Key Color
        2- Valid Incorrect Position Key Color
        3- Valid Correct Position Key Color
    """

    def __init__(self):
        self.keypad: list[Rectangle] = []
        self.letters: list[Text] = []
        self.chosen_letters = []
        #
        #   Contains the flags for each row entry the user makes
        #
        self.flags: list[list[int]] = []

    # ---------------------------------------------------------------------------------------------
    #   New Game
    #
    def new_game(self):
        self.chosen_letters.clear()
        self.flags.clear()

    # ---------------------------------------------------------------------------------------------
    #   Get Letters
    #
    def get_letter(self, index):
        return self.letters[index].label

    # ---------------------------------------------------------------------------------------------
    #   Build
    #
    def build(self):
        self.build_keypad()
        self.build_letters()

    # ---------------------------------------------------------------------------------------------
    #   Build Keypad
    #
    def build_keypad(self):
        """
        Builds the rectangular borders that represent the alpha keys of a QWERTY keyboard
        as well as the Return and Backspace keys
        """
        builder = RectangleBuilder()
        base_x_coords = [df.KeyboardBaseXR1, df.KeyboardBaseXR2, df.KeyboardBaseXR3]

        index = 0
        for row in range(df.KeyboardRows):
            for col in range(df.KeyboardColsPerRow[row]):
                kb = deepcopy(tpl.keyboard_template)

                x_coord = base_x_coords[row] + (df.KeyboardWidth + df.KeyboardGap) * col
                y_coord = df.KeyboardBaseY + (df.KeyboardHeight + df.KeyboardGap) * row

                kb['x_coord'] = x_coord
                kb['y_coord'] = y_coord
                kb['index'] = index

                index += 1
                self.keypad.append(builder.build(kb))

        self.keypad.append(builder.build(tpl.return_key_template))
        self.keypad.append(builder.build(tpl.backspace_key_template))

    # ---------------------------------------------------------------------------------------------
    #   Build Letters
    #
    def build_letters(self):
        """
        Build all the renderable letters that represent the keypad as well as the text for the
        return and backspace keys
        """
        builder = TextBuilder()
        kb_font = tpl.keyboard_font_template
        ret_font = tpl.return_font_template
        del_font = tpl.delete_font_template
        alphabet = df.qwerty

        for index in range(df.AlphabetLength):
            tmp = deepcopy(kb_font)

            tmp["label"] = alphabet[index]
            self.letters.append(builder.build(tmp))

        self.letters.append(builder.build(ret_font))
        self.letters.append(builder.build(del_font))

    # ---------------------------------------------------------------------------------------------
    #   Set Flags and Letter
    #
    def set_flags_and_letters(self, *args):
        """
        Command(SetFlagsAndLetters)
            --> WordManager(validate)
            --> set_flags_and_letters

        Used to maintain a reference to the background color the keys must maintain after
        the return key is pressed
        """
        for index, letter in enumerate(args[Index.Letters]):
            if letter not in self.chosen_letters:
                self.flags.append(args[Index.Flags][index])
                self.chosen_letters.append(args[Index.Letters][index])

    # ---------------------------------------------------------------------------------------------
    #   Update Key
    #
    def update_key(self, key):
        """
        EventHandler(GameKeypadMouseMotionHandler)
            --> update_key(key)

        Resets the background color after mouse over
        """
        if not (self.chosen_letters and self.flags):
            key.color = df.KeyAvailableColor
        else:
            keypad_letter = self.letters[key.index].label

            if keypad_letter in self.chosen_letters:
                letter_index = self.chosen_letters.index(keypad_letter)
                corresponding_flag = self.flags[letter_index]
                rect_index = df.qwerty.index(keypad_letter)

                if corresponding_flag == df.InvalidPos:
                    self.keypad[rect_index].color = df.InvalidChosenKeyColor

                if corresponding_flag == df.ValidIncorrectPos:
                    self.keypad[rect_index].color = df.ValidIncorrectPosKeyColor

                if corresponding_flag == df.ValidCorrectPos:
                    self.keypad[rect_index].color = df.ValidCorrectPosKeyColor
            else:
                key.color = df.KeyAvailableColor

    # ---------------------------------------------------------------------------------------------
    #   Update Keypad
    #
    def update_keypad(self, *args):
        """
        Command(UpdateKeypadAfterReturn)
            --> WordManager(validate)
            --> update_keypad

            The function set_flags_and_letters has to be called prior

            All flags are one-to-one with letters

            Rectangles and letters are in 1-1 correspondence
        """
        rect_indices = [df.qwerty.index(i) for i in self.chosen_letters]
        #
        #   Invalid                     = -1 --> Grey
        #   Valid Incorrect Position    = 0  --> Yellow
        #   Valid Correct Position      = 1  --> Green
        #
        for flag, index in zip(self.flags, rect_indices):
            if flag == df.InvalidPos:
                self.keypad[index].color = df.InvalidChosenKeyColor

            if flag == df.ValidIncorrectPos:
                self.keypad[index].color = df.ValidIncorrectPosKeyColor

            if flag == df.ValidCorrectPos:
                self.keypad[index].color = df.ValidCorrectPosKeyColor
