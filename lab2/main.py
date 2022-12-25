# from lab_python_oop import figure
# # from lab_python_oop import color_figure
# from lab_python_oop import square
# from lab_python_oop import rectangle
# from LAB import circle
import Lab2 as figures


def main():
    a = figures.square.Square(5, "red")
    print(a.repr())
    b = figures.rectangle.Rectangle(5, 6, "green")
    print(b.repr())
    c = figures.circle.Circle(5, "yellow")
    print(c.repr())


if (__name__ == '__main__'):
    main()