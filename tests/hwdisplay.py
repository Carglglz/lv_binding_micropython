import lvgl as lv
import pyb


class HwDisplayDriver:
    def __init__(self, width=240, height=320, color_format=lv.COLOR_FORMAT.RGB565):
        self.width = width
        self.height = height
        self.color_depth = lv.color_format_get_bpp(color_format)
        self.color_size = lv.color_format_get_size(color_format)
        self._debug = False

    @property
    def debug(self):
        return self._debug

    @debug.setter
    def debug(self, x):
        self._debug = x

    def blit(self, x1, y1, w, h, buff):
        pyb.LED((y1 % 4) + 1).toggle()
        ...


display = HwDisplayDriver()
