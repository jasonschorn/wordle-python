# -------------------------------------------------------------------------------------------------
#   All constants as well as commonly used values throughout the game
#
#
# -------------------------------------------------------------------------------------------------
#   Screen
#
ScreenWidth = 600
ScreenHeight = 750
ScreenDimensions = (600,750)
# -------------------------------------------------------------------------------------------------
#   Images
splash_screen_logo = "src/assets/wordle_splash_logo.png"
#
# -------------------------------------------------------------------------------------------------
#   Frame Rate
#
Fps = 60
main_font = "src/assets/fonts/MonaspiceRnNerdFont-Regular.otf"
splash_font = "src/assets/fonts/BigBlueTerm437NerdFont-Regular.ttf"
# -------------------------------------------------------------------------------------------------
#   Wordle Board Dimensions
#
BoardRows = 6
BoardCols = 5
# -------------------------------------------------------------------------------------------------
#   Used to determine tile color after the user enters a word
#
InvalidPos = -1
ValidIncorrectPos = 0
ValidCorrectPos = 1

MaxLetters = 5
# -------------------------------------------------------------------------------------------------
#   COLORS
#
#   Splash Screen Wordle Logo
#
SplashLogoColor = (0, 120, 200)
SplashLogoShadowColor = (200, 200, 200)
#
#   Board Button Colors
#
ButtonBgColor = (150, 150, 150)
ButtonBorderColor = (255, 255, 255)
ButtonMouseOverColor = (175, 175, 175)
ButtonFontColor = (0, 0, 0)
#
#   Fonts
#
FontColor = (248, 248, 248)
KeyFontColor = (0,0,0)
#
#   Board
#
BgColor = (18, 18, 19)
BorderColor = (58, 58, 60)
#
#   Input Validation Colors Keypad
#
KeyAvailableColor = (129, 131, 132)
ValidCorrectPosKeyColor = (83, 141, 78)
ValidIncorrectPosKeyColor = (181, 159, 59)
InvalidChosenKeyColor = (58, 58, 60)
#
#   Input Validation Colors Board
#
ValidCorrectPosColor = (83, 141, 78)
ValidIncorrectPosColor = (181, 159, 59)
InvalidPosColor = (58, 58, 60)
# -------------------------------------------------------------------------------------------------
# Font Sizes
#
BoardFontSize = 22
KeyboardFontSize = 18
RetDelKeyFontSize = 14
GameButtonFontSize = 16
# -------------------------------------------------------------------------------------------------
#   TILES
#
#   Wordle Tiles
#
BoardRectangleWidth = 60
BoardHeight = 60
BoardThickness = 2
BoardCurve = 0
#
#   Keypad Tiles
#
KeyboardWidth = 40
KeyboardHeight = 50
KeyboardThickness = 0
KeyboardCurve = 4
#
#   Board Guess Tiles
#
BoardGuessTileWidth = 52
BoardGuessTileHeight = 52
BoardGuessTileThickness = 0
BoardGuessTileCurve = 0
#
#   Keypad Guess Tiles
#
KeypadGuessTileWidth = 38
KeypadGuessTileHeight = 48
KeypadGuessTileThickness = 0
KeypadGuessTileCurve = 4
# -------------------------------------------------------------------------------------------------
#   Buttons
#
GameButtonWidth = 80
GameButtonHeight = 30
GameButtonThickness = 0
GameButtonBorderThickness = 2
GameButtonCurve = 0
GameButtonBorderCurve = 4
GameButtonGap = 20
GameButtonYOffset = 20
# -------------------------------------------------------------------------------------------------
#   Keypad Extras
#
ReturnPos = 19
AlphabetLength = 26
ReturnKeyIndex = 26
BackspaceKeyIndex = 27
# -------------------------------------------------------------------------------------------------
#   Return & Delete Keys
#
RetDelKeyWidth = 80
RetDelKeyHeight = 50
RetDelKeyThickness = 0
RetDelKeyCurve = 4
# -------------------------------------------------------------------------------------------------
#   LAYOUTS
#
#   Splash
#
SplashX = ScreenWidth / 2
SplashY = 200
#   Board Layout
#
BoardGap = 10
KeyboardGap = 5
BoardToKeyboardGap = 20
BoardBaseX = (ScreenWidth / 2 - 2 * (BoardRectangleWidth + BoardGap)) - BoardRectangleWidth / 2
BoardBaseY = 50
#
#   Kaypad Layout
#
KeyboardRows = 3
KeyboardColsPerRow = (10, 9, 7)
KeyboardBaseXR1 = (ScreenWidth/2 - 5*(KeyboardWidth + KeyboardGap)) - KeyboardGap/2
KeyboardBaseXR2 = (ScreenWidth/2 - 4*(KeyboardWidth + KeyboardGap)) - KeyboardWidth/2
KeyboardBaseXR3 = (ScreenWidth/2 - 3*(KeyboardWidth + KeyboardGap)) - KeyboardWidth/2
KeyboardBaseY = BoardBaseY + BoardRows * (BoardHeight + BoardGap) + BoardToKeyboardGap
#
#   Return & Backspace Layout
#
#       Add Return Key to the left boundary og keyboard row 3
#       Add Backspace Key to the right boundary of keyboard row 3
#
ReturnKeyX = KeyboardBaseXR3 - (RetDelKeyWidth + KeyboardGap)
DeleteKeyX = KeyboardBaseXR3 + 7 * (KeyboardWidth + KeyboardGap)
RetDelKeyY = KeyboardBaseY + 2 * (KeyboardHeight + KeyboardGap)
# -------------------------------------------------------------------------------------------------
#   Game Buttons Layout
#
#       Initial Game State --> Splash Screen
#
PlayButtonX = (ScreenWidth - GameButtonWidth) / 2
PlayButtonY = ScreenHeight - 100
# -------------------------------------------------------------------------------------------------
#   Game Buttons Layout
#
#       Play Game State
#
#           The New button is centered to the screen width and the other two button are
#           positioned around the New button
#
NewButtonX = (ScreenWidth - GameButtonWidth) / 2
NewButtonY = ScreenHeight - GameButtonHeight - GameButtonYOffset
StartButtonX = ((ScreenWidth - GameButtonWidth) / 2) - GameButtonWidth - GameButtonGap
StartButtonY = ScreenHeight - GameButtonHeight - GameButtonYOffset
QuitButtonX = ((ScreenWidth - GameButtonWidth) / 2) + GameButtonWidth + GameButtonGap
QuitButtonY = ScreenHeight - GameButtonHeight - GameButtonYOffset
# -------------------------------------------------------------------------------------------------
#   Alphabet
#
qwerty = [
    "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P",
    "A", "S", "D", "F", "G", "H", "J", "K", "L",
    "Z", "X", "C", "V", "B", "N", "M"
]
# -------------------------------------------------------------------------------------------------
#
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# -------------------------------------------------------------------------------------------------
#   Pygame Events
#
used_pygame_events = {
    "K_RETURN": 13,
    "K_BACKSPACE": 8,
    "K_ESCAPE": 27,
    "KEYDOWN": 768,
    "MOUSEBUTTONUP": 1026,
    "MOUSEMOTION": 1024
}
#
#   Map of Pygame Alpha keys to their numeric representation
#
alpha_keymap = {
    "K_A": 97,
    "K_B": 98,
    "K_C": 99,
    "K_D": 100,
    "K_E": 101,
    "K_F": 102,
    "K_G": 103,
    "K_H": 104,
    "K_I": 105,
    "K_J": 106,
    "K_K": 107,
    "K_L": 108,
    "K_M": 109,
    "K_N": 110,
    "K_O": 111,
    "K_P": 112,
    "K_Q": 113,
    "K_R": 114,
    "K_S": 115,
    "K_T": 116,
    "K_U": 117,
    "K_V": 118,
    "K_W": 119,
    "K_X": 120,
    "K_Y": 121,
    "K_Z": 122
}
