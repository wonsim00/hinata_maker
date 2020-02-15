from utils import resource_path

class animation:
    __obj = None

    def __init__(self, *args, **kwargs):
        self.__screenwidth = 0
        self.__screenheight = 0
        self.__imagewidth = 0
        self.__imageheight = 0
        self.__scheduler = None
    
    def __create_scheduler(self):
        assert self.__imagewidth and self.__imageheight
        assert self.__screenwidth and self.__screenheight

        im_w, im_h = self.__imagewidth, self.__imageheight
        sc_w, sc_h = self.__screenwidth, self.__screenheight

        x_range = (-im_w, sc_w, 9)
        y_const = sc_h-im_h-50
        flip_flop = False
        while True:
            for x in range(*x_range):
                yield (flip_flop, x, y_const)
                flip_flop = not flip_flop
    
    def get_images_path(self):
        return [
            (resource_path('hajime0.gif'), 'GIF'),
            (resource_path('hajime1.gif'), 'GIF')]

    @staticmethod
    def get_animation():
        if not animation.__obj:
            animation.__obj = animation()
        return animation.__obj
    
    def get_next_state(self):
        if not self.__scheduler:
            self.__scheduler = self.__create_scheduler()
        return next(self.__scheduler)
    
    def set_screensize(self, width, height):
        if self.__screenwidth and self.__screenheight:
            return
        self.__screenwidth = width
        self.__screenheight = height
    
    def set_imagesize(self, width, height):
        if self.__imagewidth and self.__imageheight:
            return
        self.__imagewidth = width
        self.__imageheight = height
