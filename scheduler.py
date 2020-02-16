from utils import resource_path

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

class walking_scheduler(base_scheduler):
    def __init__(self):
        super(walking_scheduler, self).__init__([
            (resource_path('hajime0.gif'), 'GIF'),
            (resource_path('hajime1.gif'), 'GIF')
        ])
    
    def _create_scheduler(self):
        im_w = self._image_width
        im_h = self._image_height
        sc_w = self._screen_width
        sc_h = self._screen_height

        assert im_w and im_h and sc_w and sc_h

        x_range = (-im_w, sc_w, 9)
        y_const = sc_h-im_h-50
        def next_idx():
            while True:
                for y in range(len(self._images_path)):
                    yield y+self._start_idx
        next_idx_gen = next_idx()

        while True:
            for x in range(*x_range):
                yield (next(next_idx_gen), x, y_const)
