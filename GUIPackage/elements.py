from .color import *
from pygame.surface import Surface

class Button:
    def __init__(self, height : int, width : int, onpress = None):
        self.height = height
        self.width = width
        self.onpress = onpress

class Element:
    def __init__(self, height : int, width : int):
        self.height = height
        self.width = width

class Font:
    Default = lambda: Font('arial', 20)
    def __init__(self, name : str, size : float):
        self.name = name
        self.size = size

class Frame:
    def __init__(self, height : int, width : int, c : list[int] = black, subElements : list[Element] = []):
        self.height = height
        self.width = width
        self.subElements = subElements
    
    def addButton(self, button : Button = None):
        pass

    @classmethod
    def FromWin(self, win):
        return Frame(win.height, win.width)

class Page(Frame):
    def __init__(self, height: int, width: int, c : list[int] = black, subElements: list[Element] = []):
        super().__init__(height, width, subElements=subElements)
        self.sprite = Surface((width, height))
        self.sprite.fill(c)
    
    def pushOnWindow(self, win):
        win.swapPage(self)
    
    @classmethod
    def FromWin(self,win):
        return Page(win.height, win.width, c = win.bc)