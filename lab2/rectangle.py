from . import figure
from . import color_figure


class Rectangle(figure.Figure):
    def __init__(self, a, b, color):
        self.a = a
        self.b = b
        self.color = color_figure.Color(color)

    FIGURE_TYPE = "Rectangle"

    def Get_Square(self):
        return self.a * self.b
