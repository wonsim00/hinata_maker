class base_scheduler:
    def __init__(self, images_path):
        self._images_path = images_path
        self._generator = None

        self._start_idx = 0
        self._image_width = 0
        self._image_height = 0
        self._screen_width = 0
        self._screen_height = 0
    
    def _create_scheduler(self, *args, **kwargs):
        raise NotImplementedError

    def get_images_path(self):
        return self._images_path[:]
    
    def set_parameters(self, **kwargs):
        for key in kwargs:
            setattr(self, "_{}".format(key), kwargs[key])
    
    def reset_scheduler(self, *args, **kwargs):
        self._generator = self._create_scheduler(*args, **kwargs)
    
    def get_next_state(self, *args, **kwargs):
        if not self._generator:
            self.reset_scheduler(*args, **kwargs)
        return next(self._generator)