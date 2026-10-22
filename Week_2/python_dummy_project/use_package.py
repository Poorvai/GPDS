# Uses our own package 'shapes' (folder with __init__.py).

import shapes
from shapes import circle_area, rectangle_area

if __name__ == "__main__":
    print("Package version:", shapes.__version__)
    print("Circle area (r=3):", round(circle_area(3), 2))
    print("Rectangle area (4 x 5):", rectangle_area(4, 5))
