from asciimatics.effects import Print, Clock, Julia
from asciimatics.renderers import FigletText, Rainbow, Plasma
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError
import sys

from dyna_figlet_effect import DynaFiglet
from my_effect import MyEffect


def demo(screen):

    effects = [
        # Julia(screen),
        Print(screen,
              Plasma(screen.height, screen.width, screen.colours),
              0,
              speed=1,
              transparent=False),
        DynaFiglet(screen, y=5)
        # MyEffect(screen),
        # Julia(screen),
        # Print(screen, Rainbow(screen, FigletText("256 colours")),
        #       y=screen.height//2 - 8),
        # Clock(screen, screen.width//2, screen.height//2, screen.height//2),
    ]
    screen.play([Scene(effects, -1)], stop_on_resize=True)


while True:
    try:
        Screen.wrapper(demo)
        sys.exit(0)
    except ResizeScreenError:
        pass
