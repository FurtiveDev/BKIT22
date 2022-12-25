from . import figure
from . import color_figure
from math import pi


class Circle(figure.Figure):
    def __init__(self, r, color):
        self.r = r
        self.color = color_figure.Color(color)

    FIGURE_TYPE = "Circle"

    def Get_Square(self):
        return round(pi * self.r ** 2)