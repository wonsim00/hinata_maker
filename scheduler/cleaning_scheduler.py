from .base_scheduler import base_scheduler

class cleaning_scheduler(base_scheduler):
    def __init__(self):
        super(cleaning_scheduler, self).__init__([
            ('sprites/hajime_right_0.gif', 'GIF'),
            ('sprites/hajime_right_1.gif', 'GIF'),
            ('sprites/hajime_left_0.gif', 'GIF'),
            ('sprites/hajime_left_1.gif', 'GIF')
        ], "Cleaning Mode")
    
    def _create_scheduler(self):
        im_w = self.image_width
        im_h = self.image_height
        sc_w = self.screen_width
        sc_h = self.screen_height

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
                yield (self.start_index+int(odd), x, y_const)
                odd = not odd
            for x in range(*x_range_dec):
                yield (self.start_index+2+int(odd), x, y_const)
                odd = not odd