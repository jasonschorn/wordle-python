from copy import deepcopy
import src.assets.templates as tpl
import pygame as pg

__all__ = ["Button"]


# -------------------------------------------------------------------------------------------------
#   Button
#
#       Class for creating the Nav buttons as well as Keypad buttons
#
class Button:
    def __init__(self):
        self.x = None
        self.y = None
        self.w = None
        self.h = None
        self.button_color = None
        self.button_thickness = None
        self.button_curve = None
        self.border_color = None
        self.border_thickness = None
        self.border_curve = None
        self.button_rectangle = None
        self.border_rectangle = None
        self.label = None
        self.font = None
        self.font_path = None
        self.font_size = None
        self.font_color = None
        self.antialias = None
        #
        # COMPUTED ATTRIBUTES
        #
        self.font_object = None
        self.renderable_font = None
        self.font_rectangle = None

    # ---------------------------------------------------------------------------------------------
    #   Button Builder
    #
    def build(self, template):
        for k, v in template.items():
            if hasattr(self, k):
                setattr(self, k, v)
        # -----------------------------------------------------------------------------------------
        # BUTTON
        self.button_rectangle = pg.Rect(self.x, self.y, self.w, self.h)
        # -----------------------------------------------------------------------------------------
        # BORDER
        if self.border_color:
            self.border_rectangle = pg.Rect(
                self.x - self.border_thickness,
                self.y - self.border_thickness,
                self.w + 2 * self.border_thickness,
                self.h + 2 * self.border_thickness
            )
        # -----------------------------------------------------------------------------------------
        # FONT OBJECT
        try:
            pg.font.init()
            self.font_object = pg.font.Font(self.font_path, self.font_size)
        except FileNotFoundError:
            try:
                self.font_object = pg.font.SysFont(self.font_path, self.font_size)
            except FileNotFoundError:
                pass
            else:
                self.font_object = pg.font.Font(None, self.font_size)
        # -----------------------------------------------------------------------------------------
        # RENDERABLE OBJECT
        self.renderable_font = self.font_object.render(self.label, self.antialias, self.font_color)
        # -----------------------------------------------------------------------------------------
        # FONT RECTANGLE
        self.font_rectangle = self.renderable_font.get_rect(center=self.button_rectangle.center)

    # -------------------------------------------------------------------------------------------------
    #   Draw a button
    #
    def draw(self, canvas):
        if self.border_color:
            pg.draw.rect(canvas, self.border_color, self.border_rectangle, self.border_thickness, self.border_curve)

        pg.draw.rect(canvas, self.button_color, self.button_rectangle, self.button_thickness, self.button_curve)
        canvas.blit(self.renderable_font, self.font_rectangle)


# -------------------------------------------------------------------------------------------------
#   Nav Button Manager
#
#       Used in State Manager
#
class NavButtonManager:
    def __init__(self):
        self.game_buttons: dict[str, Button] = {}

    # ---------------------------------------------------------------------------------------------
    #   Generate all the navigation buttons used throughout the game
    #
    def generate(self):
        for name, coords in tpl.game_button_name_and_coords.items():
            tmp = Button()
            template = deepcopy(tpl.game_button_template)
            template['x'] = coords[0]
            template['y'] = coords[1]
            template['text'] = name
            tmp.build(template)
            self.game_buttons[name] = tmp
