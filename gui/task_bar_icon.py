import wx
import wx.adv as adv

from utils import resource_path
from .menu import gif_menu

class gif_task_bar_icon(adv.TaskBarIcon):
    """
    Defines wx.adv.TaskBarIcon (icon displayed at system tray)
    for controlling gif_frame object.
    """

    def __init__(self, app):
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
        """
        Creates gif_menu object for popup menu.
        """
        return gif_menu(self.__app)
    
    def OnRightDown(self, event):
        """
        Executed when right-click event on gif_task_bar_icon object is detected.
        It creates popup menu for controlling the app.
        """
        menu = self.CreatePopupMenu()
        self.PopupMenu(menu)
        menu.Destroy()