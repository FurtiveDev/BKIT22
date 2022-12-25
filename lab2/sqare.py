from . import rectangle
from . import color_figure


class Square(rectangle.Rectangle):

    def __init__(self, a, color):
        self.a = a
        self.b = a
        self.color = color_figure.Color(color)

    FIGURE_TYPE = "Square"

    def Get_Square(self):
        return super().Get_Square()
