from src.assets.definitions import main_font
from enum import IntEnum
import pygame as pg


# -------------------------------------------------------------------------------------------------
#
#
class Index(IntEnum):
    LABEL = 0
    COLOR = 1
    SIZE = 2
    ANTIALIAS = 3
    MOUSE_OVER_COLOR = 4


# -------------------------------------------------------------------------------------------------
#   Text Setter
#
class TextSetter:
    def __init__(self):
        self.label = None
        self.color = None
        self.size = None
        self.antialias = None
        self.font_family = None
        # Used in keyboard.py
        self.pos = None

    # ---------------------------------------------------------------------------------------------
    #
    def set_label(self, label):
        self.label = label
        return self

    def set_color(self, color):
        self.color = color
        return self

    def set_antialias(self, antialias):
        self.antialias = antialias
        return self

    def set_size(self, size):
        self.size = size
        return self

    def set_font_family(self, font_family):
        self.font_family = font_family
        return self

    def set_pos(self, pos):
        self.pos = pos
        return self

    def build(self):
        return Text(self)


# -------------------------------------------------------------------------------------------------
#   Text Class
#
class Text:
    def __init__(self, setter: TextSetter):
        # SETTER
        self._label = setter.label
        self._color = setter.color
        self._size = setter.size
        self._antialias = setter.antialias
        #
        self._pos = setter.pos
        # IMPORTED
        if not setter.font_family:
            self._font_family = main_font
        else:
            self._font_family = setter.font_family
        # COMPUTED
        pg.font.init()
        self._font_object = pg.font.Font(self._font_family, self._size)
        self._renderable_text_object = self._font_object.render(self._label, self._antialias, self._color)
        self._rectangle = self._renderable_text_object.get_rect()

    # ---------------------------------------------------------------------------------------------
    #
    def __repr__(self):
        return (
            f'{self.__class__.__name__}(\n\t'
            f'text label = {self._label},\n\t'
            f'text color =  {self._color},\n\t'
            f'antialias =  {self._antialias},\n\t'
            f'size =  {self._size},\n\t'
            f'pos =  {self._pos},\n\t'
            f'font family = {self._font_family},\n\t'
            f')'
        )

    # ---------------------------------------------------------------------------------------------
    #
    @property
    def label(self) -> str:
        return self._label

    @label.setter
    def label(self, label):
        self._label = label

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, pos):
        self._pos = pos

    @property
    def font_object(self):
        return self._font_object

    @property
    def renderable_text_object(self):
        return self._renderable_text_object

    @property
    def rectangle(self):
        return self._rectangle

    @rectangle.setter
    def rectangle(self, rectangle):
        self._rectangle = rectangle

    # ---------------------------------------------------------------------------------------------
    #   Update Renderable
    #
    def update_renderable(self):
        self._font_object = pg.font.Font(self._font_family, self._size)
        self._renderable_text_object = self._font_object.render(
            self._label, self._antialias, self._color
        )
        self._rectangle = self._renderable_text_object.get_rect()

    # ---------------------------------------------------------------------------------------------
    #   Update Renderable Text Object
    #
    def update_renderable_text_object(self, label: str):
        self._label = label
        self._font_object = pg.font.Font(self._font_family, self._size)
        self._renderable_text_object = self._font_object.render(self._label, self._antialias, self._color)
        self._rectangle = self._renderable_text_object.get_rect()


# -------------------------------------------------------------------------------------------------
#   Text Builder
#
class TextBuilder:
    def __init__(self):
        self.setter = TextSetter()

    # ---------------------------------------------------------------------------------------------
    #   Build It
    #       Used in another game
    #
    def build_it(self, *args, **kwargs) -> Text:
        params = []

        if args:
            params.extend(list(args))
        elif kwargs:
            params.extend(list(kwargs.values()))
        else:
            raise Exception("Unknown parameter(s)")

        return (
            self.setter
            .set_label(params[Index.LABEL])
            .set_color(params[Index.COLOR])
            .set_size(params[Index.SIZE])
            .set_antialias(params[Index.ANTIALIAS])
        ).build()

    # ---------------------------------------------------------------------------------------------
    #   Build
    #
    def build(self, params: dict) -> Text:

        for key, value in params.items():
            if hasattr(self.setter, key):
                setattr(self.setter, key, value)

        return self.setter.build()
