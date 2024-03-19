import random
from math import cos, sin, pi

from asciimatics.effects import Effect
from datetime import datetime

class MyEffect_archived(Effect):
    # _block_char = '█'
    _block_char = '█'
    # Colour palette for 256 colour xterm mode.
    _256_palette = [196, 202, 208, 214, 220, 226, 154, 118, 82, 46, 47, 48, 49, 50, 51,
                    45, 39, 33, 27, 21, 57, 93, 129, 201, 200, 199, 198, 197, 0]

    def __init__(self, screen, left: int = 2, top: int = 2, width: int = 10, height: int = 10, **kwargs):
        """
        :param screen: The Screen being used for the Scene.
        :param c: The starting value of 'c' for the Julia Set.

        Also see the common keyword arguments in :py:obj:`.Effect`.
        """
        super().__init__(screen, **kwargs)
        self._screen= screen
        self._screen_width = screen.width
        self._screen_height = screen.height

        self._clock_left = 4
        self._clock_top = 5

        self._box_width = width
        self._box_height = height
        self._box_l = left
        self._box_t = top
        self._box_r = self._box_l + width
        self._box_b = self._box_t + height
        self._row = 0
        self._col = 0
        self._color = random.choice(MyEffect._256_palette)

    def reset(self):
        pass

    def _update(self, frame_no):
        # Get the current time
        now = datetime.now()

        # Print the formatted time with leading zeros for single-digit values
        time_str = f"{now.hour:02d}:{now.minute:02d}")

        # draw the new block
        x = self._box_l + self._col
        y = self._box_t + self._row
        self._screen.print_at(MyEffect._block_char, x, y, self._color)

        # set up next block
        self._col += 1
        if self._col >= self._box_width:
            self._col = 0
            self._row += 1
            if self._row >= self._box_height:
                self._row = 0
                # ensure we get a different new color
                c = self._color
                while c == self._color:
                    self._color = random.choice(MyEffect._256_palette)

    @property
    def stop_frame(self):
        return self._stop_frame
