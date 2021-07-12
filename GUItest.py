import GUIPackage as GUIP
from pygame import quit as Quit

def close():
    print('closed program')
    Quit()
    quit()

win = GUIP.Window(800, 600, title='test', bc = (255,255,255))

startView = GUIP.Page.FromWin(win)
startView.addButton()

win.page = startView

win.onClose = close

win.mainLoop()