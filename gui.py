import wx
import time

from animation import animation

class gif_frame(wx.Frame):
    def __init__(self, app, **kwargs):
        self.__app = app

        super(gif_frame, self).__init__(
            None,
            title = "Hinata Maker",
            style = wx.STAY_ON_TOP | wx.FRAME_SHAPED, 
            **kwargs)
        self.SetBackgroundColour("black")
    
    def OnCloseWindow(self, event):
        self.__app.keep_going = False
        self.Destroy()
    
    def prepare(self, raw_images):
        self.__images = []
        self.__regions = []

        for raw_img in raw_images:
            image = wx.StaticBitmap(
                self, bitmap = raw_img, pos = (-1, -1))
            image.Hide()

            self.__images.append(image)
            self.__regions.append(wx.Region(raw_img))
        self.__prev = -1

    def set_status(self, image_idx, x_pos, y_pos):
        self.SetShape(self.__regions[image_idx])
        self.SetPosition((x_pos, y_pos))
        self.__images[image_idx].Show()

        if self.__prev >= 0 and self.__prev != image_idx:
            self.__images[self.__prev].Hide()
        self.__prev = image_idx
        self.Show()


class gif_app(wx.App):
    def OnInit(self):
        self.__animation = animation.get_animation()
        images_path = self.__animation.get_images_path()

        assert len(images_path)
        size, images = None, []

        for path, ext in images_path:
            images.append(wx.Image(path, getattr(
                wx, "BITMAP_TYPE_{}".format(ext))).ConvertToBitmap())
            if not size:
                size = images[-1].GetSize()
            assert size == images[-1].GetSize()
        
        self.frame = gif_frame(self, size = size)
        self.__raw_images = images
        self.keep_going = True
        return True
    
    def MainLoop(self):
        err_msg = "wrapped C/C++ object of type {} has been deleted".format(
            self.frame.__class__.__name__)
        self.frame.prepare(self.__raw_images)

        image_size = self.__raw_images[0].Size
        self.__animation.set_imagesize(*image_size)
        screen_size = wx.GetDisplaySize()
        self.__animation.set_screensize(*screen_size)
        
        evtloop = wx.GUIEventLoop()
        old = wx.EventLoop.GetActive()
        wx.EventLoop.SetActive(evtloop)
        
        while self.keep_going:
            try:
                self.frame.set_status(*self.__animation.get_next_state())
            except RuntimeError as e:
                if err_msg in e.args:
                    break
                else:
                    raise e

            while evtloop.Pending():
                evtloop.Dispatch()
            
            time.sleep(0.5)
            evtloop.ProcessIdle()
        
        wx.EventLoop.SetActive(old)

if __name__ == '__main__':
    app = gif_app()
    app.MainLoop()
