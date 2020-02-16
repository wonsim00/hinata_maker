from .base_scheduler import base_scheduler

class walking_scheduler(base_scheduler):
    def __init__(self):
        super(walking_scheduler, self).__init__([
            ('hajime0.gif', 'GIF'),
            ('hajime1.gif', 'GIF')
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