from os import get_terminal_size
from pyfiglet import Figlet
from enums import Color

class Drawer:
    
    # Can choose font from -> http://www.figlet.org/fontdb.cgi
    def __init__(self, font='block', color=Color.GREEN.value):
        self.f = Figlet(font=font)
        self.color = color
    

    def draw(self, text, center=True):
        if center:
            print(
                *[
                    self.color + x.center(get_terminal_size().columns)
                    for x in self.f.renderText(text).split("\n")
                ], sep='\n'
            )
        else:
            print(self.f.renderText(text))
