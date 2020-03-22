from .base_scheduler import base_scheduler

class walking_scheduler(base_scheduler):
    def __init__(self):
        super(walking_scheduler, self).__init__([
            ('sprites/hajime_right_0.gif', 'GIF'),
            ('sprites/hajime_right_1.gif', 'GIF')
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

class return_trip_scheduler(base_scheduler):
    def __init__(self):
        super(return_trip_scheduler, self).__init__([
            ('sprites/hajime_right_0.gif', 'GIF'),
            ('sprites/hajime_right_1.gif', 'GIF'),
            ('sprites/hajime_left_0.gif', 'GIF'),
            ('sprites/hajime_left_1.gif', 'GIF')
        ])
    
    def _create_scheduler(self):
        im_w = self._image_width
        im_h = self._image_height
        sc_w = self._screen_width
        sc_h = self._screen_height

        assert im_w and im_h and sc_w and sc_h

        pixel_per_step = 9
        steps = (sc_w-im_w)//2//pixel_per_step-1
        blank = (sc_w-im_w-pixel_per_step*2*steps)//2

        x_range_inc = (
            blank+pixel_per_step, 
            blank+pixel_per_step*(2*steps+1), 
            pixel_per_step
        )
        x_range_dec = (
            blank+pixel_per_step*(2*steps-1),
            blank-pixel_per_step,
            -pixel_per_step
        )
        y_const = sc_h-im_h-50
        yield (0, blank, y_const)

        odd = True
        while True:
            for x in range(*x_range_inc):
                yield (self._start_idx+int(odd), x, y_const)
                odd = not odd
            for x in range(*x_range_dec):
                yield (self._start_idx+2+int(odd), x, y_const)
                odd = not odd
