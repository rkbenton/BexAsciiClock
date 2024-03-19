import random
from math import cos, sin, pi

from asciimatics.effects import Effect
from datetime import datetime

from asciimatics.renderers import FigletText


class MyEffect(Effect):

    def __init__(self, screen, **kwargs):
        """
        :param screen: The Screen being used for the Scene.

        Also see the common keyword arguments in :py:obj:`.Effect`.
        """
        super().__init__(screen, **kwargs)
        self._screen= screen
        self._screen_width = screen.width
        self._screen_height = screen.height

        self._clock_left = 4
        self._clock_top = 5

        # self._box_width = width
        # self._box_height = height
        # self._box_l = left
        # self._box_t = top
        # self._box_r = self._box_l + width
        # self._box_b = self._box_t + height
        # self._row = 0
        # self._col = 0
        # self._color = random.choice(MyEffect._256_palette)

    def reset(self):
        pass

    def _update(self, frame_no):
        # Get the current time
        current_time = datetime.now()

        # Print the formatted time with leading zeros for single-digit values
        time_str = f"{current_time.hour:02d}:{current_time.minute:02d}"

        rendered_text = FigletText(time_str)



    @property
    def stop_frame(self):
        return self._stop_frame
