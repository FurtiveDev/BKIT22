from abc import ABC
from abc import abstractmethod
from . import color_figure


class Figure(ABC):
    FIGURE_TYPE = ""

    def __init__(self):
        super().__init__()

    def Get_Square(self):
        pass

    def Get_type_figure(self):
        return self.FIGURE_TYPE

    def repr(self):
        return ('{} {} {}'.format(self.Get_type_figure(), self.Get_Square(), self.color.Get_Value()))

