from .handlers import GeometryHandler
from .elements import Frame, Page
from .color import *
import pygame as pg

def basicClose():
    pg.quit()
    quit()

class Window(GeometryHandler):
    def __init__(self, width : int, height : int, title : str = '', bc : tuple = black, pages : dict[str : Page] = False):
        self.width = width
        self.height = height
        self.title = title
        self.bc = bc
        self.elements = Frame(width,height)
        self.onClose = basicClose
        if not pages:
            self.pages = {'start' : Page.FromWin(self)}
        try:
            self.page = self.pages['start']
        except KeyError:
            self.pages = {'start' : Page.FromWin(self)}
            self.page = self.pages['start']
    
    def pushPage(self, page : Page):
        self.page = page

    def mainLoop(self):
        win = pg.display.set_mode((self.width, self.height))
        pg.display.set_caption(self.title)

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.onClose()
            
            win.blit(self.page.sprite, (0,0))