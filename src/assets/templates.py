# -------------------------------------------------------------------------------------------------
#   Templates used to create various game assets
#
#       Several classes use the builder pattern and I felt it was easier to use templates
#       that are in one single file for ease of updating values, it is easier to use
#       hasatr together with setatr, and it prevents having to repeatedly type out each builder:
#
#       return (
#             self.setter
#             .set_some_attribute_1(val)
#             .set_some_attribute_2(val)
#             ...
#             .set_some_attribute_k(val)
#         )
# -------------------------------------------------------------------------------------------------
from src.assets.definitions import *
# -------------------------------------------------------------------------------------------------
#   Template for all navigation buttons
#
game_button_template = {
    "x": 0,
    "y": 0,
    "w": 80,
    "h": 30,
    "button_color": ButtonBgColor,
    "button_thickness": 0,
    "button_curve": 4,
    "label": "",
    "font_path": main_font,
    "font_size": 16,
    "font_color": ButtonFontColor,
    "antialias": True
}
# -------------------------------------------------------------------------------------------------
#   Board refers to the 6x5 grid where user input is rendered
#
board_template = {
    "x_coord": 0,
    "y_coord": 0,
    "width": BoardRectangleWidth,
    "height": BoardHeight,
    "thickness": BoardThickness,
    "curve": BoardCurve,
    "color": BorderColor,
    "index": 0
}
# -------------------------------------------------------------------------------------------------
#   QWERTY game keyboard
#
keyboard_template = {
    "x_coord": 0,
    "y_coord": 0,
    "width": KeyboardWidth,
    "height": KeyboardHeight,
    "thickness": KeyboardThickness,
    "curve": KeyboardCurve,
    "color": KeyAvailableColor,
    "index": 0
}
# -------------------------------------------------------------------------------------------------
#   Colored tiles used to denote the correctness of a users guess
#
board_guess_tile_template = {
    "x_coord": 0,
    "y_coord": 0,
    "width": BoardGuessTileWidth,
    "height": BoardGuessTileHeight,
    "thickness": BoardGuessTileThickness,
    "curve": BoardGuessTileCurve,
    "color": None
}
# -------------------------------------------------------------------------------------------------
#   Same as the above but for the QWERTY keyboard
#
keypad_guess_tile_template = {
    "x_coord": 0,
    "y_coord": 0,
    "width": KeypadGuessTileWidth,
    "height": KeypadGuessTileHeight,
    "thickness": KeypadGuessTileThickness,
    "curve": KeypadGuessTileCurve,
    "color": None
}
# -------------------------------------------------------------------------------------------------
#   Return Key
#
return_key_template = {
    "x_coord": ReturnKeyX,
    "y_coord": RetDelKeyY,
    "width": RetDelKeyWidth,
    "height": RetDelKeyHeight,
    "thickness": KeyboardThickness,
    "curve": KeyboardCurve,
    "color": KeyAvailableColor,
    "index": 26
}
# -------------------------------------------------------------------------------------------------
#   Backspace Key
#
backspace_key_template = {
    "x_coord": DeleteKeyX,
    "y_coord": RetDelKeyY,
    "width": RetDelKeyWidth,
    "height": RetDelKeyHeight,
    "thickness": KeyboardThickness,
    "curve": KeyboardCurve,
    "color": KeyAvailableColor,
    "index": 27
}
# -------------------------------------------------------------------------------------------------
#   Wordle word font
#
board_font_template = {
    "label": "",
    "color": FontColor,
    "antialias": True,
    "size": BoardFontSize
}
# -------------------------------------------------------------------------------------------------
#   QWERTY keyboard font
#
keyboard_font_template = {
    "label": "",
    "color": KeyFontColor,
    "antialias": True,
    "size": KeyboardFontSize,
    "pos": 0
}
# -------------------------------------------------------------------------------------------------
#   Return key font
#
return_font_template = {
    "label": "Return",
    "color": KeyFontColor,
    "antialias": True,
    "size": RetDelKeyFontSize
}
# -------------------------------------------------------------------------------------------------
#   Backspace key font (never renamed RetDel... constants)
#
delete_font_template = {
    "label": "Delete",
    "color": KeyFontColor,
    "antialias": True,
    "size": RetDelKeyFontSize
}
# -------------------------------------------------------------------------------------------------
#   Worlde text that is displayed in Initial State
#
splash_logo_template = {
    "label": "Wordle",
    "color": SplashLogoColor,
    "antialias": True,
    "size": 120,
    "font_family": splash_font
}
# -------------------------------------------------------------------------------------------------
#   White-ish shadow for splash logo
#
splash_logo_shadow_template = {
    "label": "Wordle",
    "color": SplashLogoShadowColor,
    "antialias": True,
    "size": 120,
    "font_family": splash_font
}
# -------------------------------------------------------------------------------------------------
#   Used by Nav Button Manager in State Manager
#
game_button_name_and_coords = {
    "Start": [StartButtonX, StartButtonY],
    "New": [NewButtonX, NewButtonY],
    "Play": [PlayButtonX, PlayButtonY],
    "Quit": [QuitButtonX, QuitButtonY]
}