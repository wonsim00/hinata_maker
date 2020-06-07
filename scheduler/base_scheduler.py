class base_scheduler:
    def __init__(self, images_path, menu_name = None):
        self._images_path = images_path
        self._generator = None
        self._menu_name = menu_name if menu_name else type(self).__name__

        self.__start_index = -1
        self.__image_width = -1
        self.__image_height = -1
        self.__screen_width = -1
        self.__screen_height = -1
    
    @property
    def start_index(self):
        return self.__start_index
    @start_index.setter
    def start_index(self, value):
        if self.__start_index < 0:
            self.__start_index = value
    
    @property
    def image_width(self):
        return self.__image_width
    @image_width.setter
    def image_width(self, value):
        if self.__image_width < 0:
            self.__image_width = value
    
    @property
    def image_height(self):
        return self.__image_height
    @image_height.setter
    def image_height(self, value):
        if self.__image_height < 0:
            self.__image_height = value
    
    @property
    def screen_width(self):
        return self.__screen_width
    @screen_width.setter
    def screen_width(self, value):
        if self.__screen_width < 0:
            self.__screen_width = value
    
    @property
    def screen_height(self):
        return self.__screen_height
    @screen_height.setter
    def screen_height(self, value):
        if self.__screen_height < 0:
            self.__screen_height = value

    def _create_scheduler(self, *args, **kwargs):
        raise NotImplementedError

    def get_images_path(self):
        for image_path in self._images_path:
            yield image_path
    
    def reset_scheduler(self, *args, **kwargs):
        self._generator = self._create_scheduler(*args, **kwargs)
    
    def get_next_state(self, *args, **kwargs):
        if not self._generator:
            self.reset_scheduler(*args, **kwargs)
        return next(self._generator)