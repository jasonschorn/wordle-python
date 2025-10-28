from copy import deepcopy
from src.rectangle import Rectangle, RectangleBuilder
from src.text import Text, TextBuilder
import src.assets.definitions as df
import src.assets.templates as tpl

# -------------------------------------------------------------------------------------------------
#
#
__all__ = ["Board"]


# -------------------------------------------------------------------------------------------------
#   Board CLass
#
#       Responsible for creating and managing the 6x5 Wordle game board
#
class Board:
    def __init__(self):
        self.tiles: list[Rectangle] = []
        self.guess_tiles: list[Rectangle] = []
        self.renderable_letters: list[Text] = []
        self.row_index = 0

        self.rect_builder = RectangleBuilder()
        self.text_builder = TextBuilder()

    # -------------------------------------------------------------------------------------------------
    #   New Game
    #
    def new_game(self):
        self.guess_tiles.clear()
        self.renderable_letters.clear()
        self.row_index = 0

    # -------------------------------------------------------------------------------------------------
    #   Build
    #
    def build(self):
        index = 0
        for row in range(df.BoardRows):
            for col in range(df.BoardCols):
                rectangle = deepcopy(tpl.board_template)
                x_coord = df.BoardBaseX + (df.BoardRectangleWidth + df.BoardGap) * col
                y_coord = df.BoardBaseY + (df.BoardHeight + df.BoardGap) * row

                rectangle['x_coord'] = x_coord
                rectangle['y_coord'] = y_coord
                rectangle["index"] = index

                index += 1
                self.tiles.append(self.rect_builder.build(rectangle))

    # ---------------------------------------------------------------------------------------------
    #   Update Board
    #
    def update_board(self, flags: list[int]):
        """
            The index of each flag directly corresponds to a box on the Wordle board and is colored
            according to the rules of the game.

            Deepcopy is used to prevent overwriting the dictionary template used for all tiles
        """
        temp_tile = deepcopy(tpl.board_guess_tile_template)

        for index, flag in enumerate(flags):
            rect_index = 5 * self.row_index + index

            if flag == df.InvalidPos:
                temp_tile['color'] = df.InvalidPosColor

            if flag == df.ValidIncorrectPos:
                temp_tile['color'] = df.ValidIncorrectPosColor

            if flag == df.ValidCorrectPos:
                temp_tile['color'] = df.ValidCorrectPosColor
            #
            #
            temp_tile['x_coord'] = self.tiles[rect_index].x_coord + 2 * self.tiles[rect_index].thickness
            temp_tile['y_coord'] = self.tiles[rect_index].y_coord + 2 * self.tiles[rect_index].thickness

            self.guess_tiles.append(self.rect_builder.build(temp_tile))

        self.row_index += 1
