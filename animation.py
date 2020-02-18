from scheduler import base_scheduler, return_trip_scheduler

class animation:
    __obj = None

    def __init__(self, *scheduler_types):
        self.__imagewidth = 0
        self.__imageheight = 0
        self.__screenwidth = 0
        self.__screenheight = 0

        assert len(scheduler_types)

        self.__schedulers = []
        for typ in scheduler_types:
            temp = typ()
            assert isinstance(temp, base_scheduler)
            self.__schedulers.append(temp)
        
        self.__curr_scheduler = self.__schedulers[0]
    
    def get_images_path(self):
        return self.__curr_scheduler.get_images_path()
    
    def get_next_state(self):
        return self.__curr_scheduler.get_next_state()
    
    def set_imagesize(self, width, height):
        if self.__imagewidth and self.__imageheight:
            return
        self.__imagewidth = width
        self.__imageheight = height
        
        for scheduler in self.__schedulers:
            scheduler.set_parameters(
                image_width = width,
                image_height = height
            )    

    def set_screensize(self, width, height):
        if self.__screenwidth and self.__screenheight:
            return
        self.__screenwidth = width
        self.__screenheight = height

        for scheduler in self.__schedulers:
            scheduler.set_parameters(
                screen_width = width,
                screen_height = height
            )

    @staticmethod
    def get_animation():
        if not animation.__obj:
            animation.__obj = animation(return_trip_scheduler)
        return animation.__obj
    