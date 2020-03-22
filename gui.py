import wx
import wx.adv as adv
import time

from animation import animation
from utils import resource_path

class gif_menu(wx.Menu):
    def __init__(self, app):
        super(gif_menu, self).__init__()
        self.__app = app

        mi_exit = wx.MenuItem(self, wx.NewIdRef(), 'Exit')
        self.Bind(wx.EVT_MENU, self.OnExit, mi_exit)
        self.Append(mi_exit)
    
    def OnExit(self, event):
        wx.PostEvent(
            self.__app.frame.GetEventHandler(),
            wx.PyCommandEvent(
                wx.EVT_CLOSE.typeId, 
                self.__app.frame.GetId()
            )
        )

class gif_task_bar_icon(adv.TaskBarIcon):
    def __init__(self, app, *args):
        super(gif_task_bar_icon, self).__init__()
        self.__app = app

        img = wx.Image(
            resource_path("hajime_face.gif"),
            wx.BITMAP_TYPE_GIF
        ).ConvertToBitmap()

        self.__icon = wx.Icon(img)
        self.SetIcon(self.__icon)

        self.Bind(
            adv.EVT_TASKBAR_RIGHT_DOWN,
            self.OnRightDown
        )
    
    def CreatePopupMenu(self):
        menu = gif_menu(self.__app)
        return menu
    
    def OnRightDown(self, event):
        menu = self.CreatePopupMenu()
        self.PopupMenu(menu)
        menu.Destroy()

class gif_frame(wx.Frame):
    def __init__(self, app, **kwargs):
        super(gif_frame, self).__init__(
            None,
            title = "Hinata Maker",
            style = wx.STAY_ON_TOP | wx.FRAME_SHAPED, 
            **kwargs
        )
        self.SetBackgroundColour("black")
        self.__app = app

        self.Bind(
            wx.EVT_CLOSE,
            self.OnCloseWindow,
            self
        )
    
    def OnCloseWindow(self, event):
        self.__app.keep_going = False
        self.Destroy()
    
    def prepare(self, raw_images):
        self.__images = []
        self.__regions = []

        for raw_img in raw_images:
            image = wx.StaticBitmap(
                self, bitmap = raw_img, pos = (-1, -1)
            )
            image.Hide()

            self.__images.append(image)
            self.__regions.append(wx.Region(raw_img))
        self.__prev = -1

    def set_state(self, image_idx, x_pos, y_pos):
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
            images.append(
                wx.Image(
                    resource_path(path),
                    getattr(wx, "BITMAP_TYPE_{}".format(ext))
                ).ConvertToBitmap()
            )
            if not size:
                size = images[-1].GetSize()
            assert size == images[-1].GetSize()
        
        self.frame = gif_frame(self, size = size)
        self.__raw_images = images
        self.keep_going = True

        self.task_bar_icon = gif_task_bar_icon(self)
        return True
    
    def MainLoop(self):
        self.frame.prepare(self.__raw_images)

        image_size = self.__raw_images[0].Size
        self.__animation.set_imagesize(*image_size)
        screen_size = wx.GetDisplaySize()
        self.__animation.set_screensize(*screen_size)
        
        evtloop = wx.GUIEventLoop()
        old = wx.EventLoop.GetActive()
        wx.EventLoop.SetActive(evtloop)
        
        while self.keep_going:
            self.frame.set_state(*self.__animation.get_next_state())

            while evtloop.Pending():
                evtloop.Dispatch()
            
            time.sleep(0.5)
            evtloop.ProcessIdle()
        
        wx.EventLoop.SetActive(old)

if __name__ == '__main__':
    app = gif_app()
    app.MainLoop()
