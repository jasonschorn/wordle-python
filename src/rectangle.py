import pygame as pg


# ---------------------------------------------------------------------------------------------
#   Rectangle Setter
#
#       Similar to the text class, this is overly generalized because I use this class
#       in other programs that benefit from the generality provided by the builder pattern
#
class RectangleSetter:
    def __init__(self):
        self.x_coord = None
        self.y_coord = None
        self.width = None
        self.height = None
        # zero thickness --> filled rectangle
        self.thickness = None
        self.curve = None
        self.color = None
        self.index = None
        self.rectangle = None

    def set_x_coord(self, x_coord: int | float):
        self.x_coord = x_coord
        return self

    def set_y_coord(self, y_coord: int | float):
        self.y_coord = y_coord
        return self

    def set_width(self, width: int):
        self.width = width
        return self

    def set_height(self, height: int):
        self.height = height
        return self

    def set_thickness(self, width: int):
        self.thickness = width
        return self

    def set_curve(self, curve: int):
        self.curve = curve
        return self

    def set_color(self, color: tuple[int, int, int]):
        self.color = color
        return self

    def set_index(self, index: int):
        self.index = index
        return self

    def set_rectangle(self):
        self.rectangle = pg.Rect(self.x_coord, self.y_coord, self.width, self.height)
        return self

    def build(self):
        return Rectangle(self)


# -------------------------------------------------------------------------------------------------
#   Rectangle Class
#
class Rectangle:
    def __init__(self, setter: RectangleSetter):
        self.setter = setter
        self._x_coord = setter.x_coord
        self._y_coord = setter.y_coord
        self._width = setter.width
        self._height = setter.height
        self._thickness = setter.thickness
        self._curve = setter.curve
        self._color = setter.color
        self._index = setter.index

        if setter.rectangle:
            self._rectangle = setter.rectangle
        else:
            self._rectangle = self.set_rectangle()

    # ---------------------------------------------------------------------------------------------
    #   Repr
    def __repr__(self):
        return (f"{self.__class__.__name__}("
                f"x= {self._x_coord}, "
                f"y= {self._y_coord}, "
                f"w= {self._width}, "
                f"h= {self._height}, "
                f"col= {self._color}, "
                f"t= {self._thickness}, "
                f"cur= {self._curve}, "
                f"index= {self._index}, "
                f"rect= {self._rectangle}"
                f"")

    # -------------------------------------------------------------------------------------------------
    #   Properties
    @property
    def x_coord(self):
        return self._x_coord

    @x_coord.setter
    def x_coord(self, x_coord):
        self._x_coord = x_coord

    @property
    def y_coord(self):
        return self._y_coord

    @y_coord.setter
    def y_coord(self, y_coord):
        self._y_coord = y_coord

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color: tuple[int, int, int]):
        self._color = color

    @property
    def thickness(self):
        return self._thickness

    @property
    def curve(self):
        return self._curve

    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, index):
        self._index = index

    @property
    def rectangle(self):
        return self._rectangle

    @rectangle.setter
    def rectangle(self, rectangle):
        self._rectangle = rectangle

    def set_rectangle(self):
        return pg.Rect(self._x_coord, self._y_coord, self._width, self._height)


# -------------------------------------------------------------------------------------------------
#   Rectangle Builder
#
class RectangleBuilder:
    def __init__(self):
        self.setter = RectangleSetter()

    # -------------------------------------------------------------------------------------------------
    #   Build
    def build(self, params: dict) -> Rectangle:
        for key, value in params.items():
            if hasattr(self.setter, key):
                setattr(self.setter, key, value)

        return self.setter.build()

    # -------------------------------------------------------------------------------------------------
    #   Banner
    #
    #       TODO --> Finish or remove
    def banner(self, x, y, w, h, color, thickness, curve):
        return (
            self.setter
            .set_x_coord(x)
            .set_y_coord(y)
        )
