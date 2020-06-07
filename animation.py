from scheduler import base_scheduler, return_trip_scheduler

class animation:
    __obj = None

    def __init__(self, *scheduler_types):
        super(animation, self).__init__()
        assert len(scheduler_types)

        self.__schedulers = []
        for typ in scheduler_types:
            temp = typ()
            assert isinstance(temp, base_scheduler)
            self.__schedulers.append(temp)
        
        self.__curr_index = 0
        self.__curr_scheduler = self.__schedulers[self.__curr_index]
    
    def get_next_state(self):
        return self.__curr_scheduler.get_next_state()
    
    def get_schedulers(self):
        for scheduler in self.__schedulers:
            yield scheduler

    def set_curr_scheduler(self, index: int):
        if self.__curr_index == index:
            return
        self.__curr_index = index
        self.__curr_scheduler = self.__schedulers[index]
        self.__curr_scheduler.reset_scheduler()
    
    def set_imagesize(self, *images_size):
        for image_size, scheduler in zip(images_size, self.__schedulers):
            image_width, image_height = image_size
            scheduler.image_width = image_width
            scheduler.image_height = image_height

    def set_screensize(self, width: int, height: int):
        for scheduler in self.__schedulers:
            scheduler.screen_width = width
            scheduler.screen_height = height

    @staticmethod
    def get_animation():
        if not animation.__obj:
            animation.__obj = animation(return_trip_scheduler)
        return animation.__obj
    