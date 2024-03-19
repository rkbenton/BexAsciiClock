from datetime import datetime

from asciimatics import constants
from asciimatics.effects import Effect
from asciimatics.renderers import FigletText


class DynaFiglet(Effect):
    """
    Special effect to using Cycle as a framework
    """

    # def __init__(self, screen, renderer, y, **kwargs):
    def __init__(self, screen, x=10, y=10, **kwargs):
        """
        :param screen: The Screen being used for the Scene.
        :param renderer: The Renderer which is to be cycled.
        :param y: The line (y coordinate) for the start of the text.

        Also see the common keyword arguments in :py:obj:`.Effect`.
        """
        super().__init__(screen, **kwargs)
        # self._renderer = renderer
        self._y = y
        self._x = x
        self._colour = constants.COLOUR_YELLOW
        self._last_time_str = ""
        self._rendered_text = None
        self._font = "doh"  # "Colossal"

    def reset(self):
        pass

    def _update(self, frame_no):
        # if frame_no % 2 == 0:
        #     return

        # Get the current time
        current_time = datetime.now()

        # Print the formatted time with leading zeros for single-digit values
        a_time_str = f"{current_time.hour:02d}:{current_time.minute:02d}:{current_time.second:02d}"
        if self._last_time_str != a_time_str:
            self._last_time_str = a_time_str
            self._rendered_text = FigletText(self._last_time_str,font=self._font)  # NB: this is derived from StaticRenderer

        y = self._y
        # image, _ = self._renderer.rendered_text
        image, _ = self._rendered_text.rendered_text
        for line in image:
            if self._screen.is_visible(0, y):
                # self._screen.centre(line, y, self._colour)
                self._screen.paint(line, self._x, y, colour=self._colour, transparent=True)
            y += 1
        # self._colour = (self._colour + 1) % 8

    @property
    def stop_frame(self):
        return 0
