import wx
import time

from utils import resource_path
from animation import animation
from .app_abstract import gif_app_abstract
from .frame import gif_frame
from .task_bar_icon import gif_task_bar_icon

class gif_app(gif_app_abstract):
    """
    Defines wx.App object that controls the animated gif images.
    """

    def OnInit(self):
        """
        Initializes the app.
        """
        self.__animation = animation.get_animation()
        images_path = self.__animation.get_images_path()

        assert len(images_path)
        size, images = None, []

        for path, ext in images_path:
            images.append(
                wx.Image(
                    resource_path(path),
                    getattr(wx, "BITMAP_TYPE_{}".format(ext))
                ).ConvertToBitmap()
            )
            if not size:
                size = images[-1].GetSize()
            assert size == images[-1].GetSize()
        
        self.__frame = gif_frame(self, size = size)
        self.__raw_images = images

        self.__task_bar_icon = gif_task_bar_icon(self)
        return True
    
    @property
    def frame(self):
        return self.__frame
    
    @property
    def task_bar_icon(self):
        return self.__task_bar_icon
    
    def MainLoop(self):
        """
        App execution function
        """
        self.frame.prepare(self.__raw_images)

        image_size = self.__raw_images[0].Size
        self.__animation.set_imagesize(*image_size)
        screen_size = wx.GetDisplaySize()
        self.__animation.set_screensize(*screen_size)
        
        evtloop = wx.GUIEventLoop()
        old = wx.EventLoop.GetActive()
        wx.EventLoop.SetActive(evtloop)
        
        while self._keep_going:
            self.frame.set_state(*self.__animation.get_next_state())

            while evtloop.Pending():
                evtloop.Dispatch()
            
            time.sleep(0.5)
            evtloop.ProcessIdle()
        
        wx.EventLoop.SetActive(old)