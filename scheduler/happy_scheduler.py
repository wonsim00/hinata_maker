from .base_scheduler import base_scheduler

class happy_scheduler(base_scheduler):
    def __init__(self):
        super(happy_scheduler, self).__init__([
            ('sprites/hajime_happy_0.gif', 'GIF'),
            ('sprites/hajime_happy_1.gif', 'GIF')
        ])
    
    def _create_scheduler(self):
        x_const = 100
        y_const = 500
        odd = False
        while True:
            yield (odd, x_const, y_const)
            odd = not odd