from copy import deepcopy
from random import choice
from src.board import Board
from src.commands import UpdateBoardAfterReturn
from src.commands import UpdateKeypadAfterReturn
from src.commands import SetFlagsAndLetters
from src.keyboard import Keyboard
from src.text import TextBuilder

import src.assets.definitions as df
import src.assets.templates as tpl
import src.wordle_words as words
# ---------------------------------------------------------------------------------------------====
#
#
__all__=["WordManager"]
# ---------------------------------------------------------------------------------------------====
#
#
class WordManager:
    """

    """

    # ---------------------------------------------------------------------------------------------
    #   Prevents the possibility of getting the same word during a series of games
    #
    prior_words_to_find = []


    def __init__(self, board: Board, keypad: Keyboard):
        # -----------------------------------------------------------------------------------------
        #   Randomly chosen word from words.json
        #
        self.wordle_word = None
        # -----------------------------------------------------------------------------------------
        #   List of the current set of letters chosen by the user
        #   List of words chosen by the user
        #   List of renderable letters corresponding to each chosen word
        #
        self.chosen_letters = []
        self.chosen_words = []
        self.renderable_letters = []
        self.text_builder = TextBuilder()
        # -----------------------------------------------------------------------------------------
        #   Commands
        #
        self.update_board_command = UpdateBoardAfterReturn(board)
        self.update_keypad_command = UpdateKeypadAfterReturn(keypad)
        self.set_flags_and_letters_command = SetFlagsAndLetters(keypad)

        self.curCol = 0
        self.curRectIndex = 0
        self.game_over = False
    # ---------------------------------------------------------------------------------------------
    #   New Game
    #
    def new_game(self):
        """
            Resets instance attributes and retrieves a new Wordle Word.
                1- Clears chosen letters
                2- Clears chosen words
                3- Clears renderable letters
                4- Sets current column to 0
                5- Sets current rectangle index to 0
                6- Sets game over to false
        """
        self.set_wordle_word()
        self.chosen_letters.clear()
        self.chosen_words.clear()
        self.renderable_letters.clear()
        self.curCol = 0
        self.curRectIndex = 0
        self.game_over = False
    # ---------------------------------------------------------------------------------------------
    # Set Wordle Word
    #
    def set_wordle_word(self):
        """
            Randomly choose a new Wordle Word and append this word
            to the list of words that have already been chosen.
        """
        chosen = choice(words.all_words)

        if chosen not in self.prior_words_to_find:
            self.prior_words_to_find.append(chosen)
        else:
            self.set_wordle_word()

        self.wordle_word = chosen.upper()
    # ---------------------------------------------------------------------------------------------
    #   Add Letter
    #
    def add_letter(self, letter: str):
        """
            Takes user input and adds the current chosen letter to the
            chosen letters list as well as creates a renderable version of
            the letter and adds it to the renderable letter list.
        """

        print(len(self.chosen_letters))
        if len(self.chosen_letters) < df.MaxLetters:
            # -------------------------------------------------------------------------------------
            #   Add <letter> to the current list of chosen letters
            #
            self.chosen_letters.append(letter)
            # -------------------------------------------------------------------------------------
            #   Use <letter> to create a renderable text object
            #
            new_letter = deepcopy(tpl.board_font_template)
            new_letter["label"] = letter
            self.renderable_letters.append(self.text_builder.build(new_letter))

            self.curRectIndex += 1
            self.curCol += 1

        print(len(self.chosen_letters))

    # ---------------------------------------------------------------------------------------------
    #   Remove Letter
    #
    def remove_letter(self):
        """
            Corresponds to backspace key and removes a single letter from
            the chosen letter and renderable letters lists.
        """
        if len(self.chosen_letters) > 0:
            self.chosen_letters.pop()
            self.renderable_letters.pop()
            self.curRectIndex -= 1
            self.curCol -= 1
    # ---------------------------------------------------------------------------------------------
    #   Validate
    #
    def validate(self):
        """
            Only perform validation if the user has entered all 5 letters
        """
        if not self.game_over:
            if self.curCol == 5:
                #   TODO --> add function to check if the word entered is defined in wordle word list
                #
                flags = self.get_flags()
                # ---------------------------------------------------------------------------------
                #   Command --> Board.update_board
                #   Command --> Keyboard.update_keypad
                #
                self.update_board_command.execute(flags)
                self.set_flags_and_letters_command.execute(flags, self.chosen_letters)
                self.update_keypad_command.execute()
                # ---------------------------------------------------------------------------------
                #
                #
                if all(list(map(lambda x: x == 1, flags))):
                    # -----------------------------------------------------------------------------
                    #   All flags == 1 --> the correct word was found now end the game with a
                    #   congrats message
                    #
                    self.game_over = True

                elif self.curRectIndex == 29:
                    # -----------------------------------------------------------------------------
                    #   This occurs when the user has reached row 6, has entered 5 letters and
                    #   pressed return.  Since the above condition was not met (i.e., all flags == 1),
                    #   then it follows that the final word entered is NOT the correct word and the
                    #   user has lost the game.
                    self.game_over = True

                else:
                    self.chosen_words.append("".join(self.chosen_letters))
                    self.chosen_letters.clear()
                    self.curCol = 0
    # ---------------------------------------------------------------------------------------------
    #   Find Occurrences
    #
    @staticmethod
    def find_occurrences(char: str, word: list[str]) -> list[int]:
        return [index for (index, char_in_word) in enumerate(word) if char == char_in_word]
    # ---------------------------------------------------------------------------------------------
    #   Find Indices
    #
    @staticmethod
    def find_indices(item, lst):
        return [index for index, val in enumerate(lst) if val == item ]
    # ---------------------------------------------------------------------------------------------
    #   Get Flags
    #
    def get_flags(self) -> list[int]:
        found = []
        flags = [df.InvalidPos, df.InvalidPos, df.InvalidPos, df.InvalidPos, df.InvalidPos,]
        w_word = list(self.wordle_word)

        for index, (char_in_guess, char_in_word) in enumerate(zip(self.chosen_letters, w_word)):
            if char_in_guess == char_in_word:
                flags[index] = df.ValidCorrectPos
                found.append(index)

        for index, char in enumerate(self.chosen_letters):
            if char in w_word and flags[index] != df.ValidCorrectPos:
                occurrences = self.find_occurrences(char, w_word)

                for pos in occurrences:
                    if pos not in found:
                        flags[index] = df.ValidIncorrectPos
                        found.append(pos)
                        break

        return flags
