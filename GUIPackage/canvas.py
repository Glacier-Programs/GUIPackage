from .elements import Element

class Canvas(Element):
    def __init__(self, height: int, width: int):
        super().__init__(height, width)