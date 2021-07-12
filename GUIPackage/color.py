from pygame import Color
from random import randint

randVal = lambda : randint(0,255)
randColor = lambda : Color(randVal(),randVal(),randVal())
randRGBA = lambda : Color(randVal(), randVal(), randVal(), randVal())

black = Color(0,0,0)
