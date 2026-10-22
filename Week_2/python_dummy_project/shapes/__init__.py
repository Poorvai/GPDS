# Package entry point: makes 'shapes' importable and exposes its functions.

from .circle import circle_area
from .rectangle import rectangle_area

__all__ = ["circle_area", "rectangle_area"]
__version__ = "0.1.0"
