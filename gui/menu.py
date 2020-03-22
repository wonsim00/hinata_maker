import wx

class gif_menu(wx.Menu):
    """
    Defines wx.Menu object for gif_task_bar_icon.
    """

    def __init__(self, app):
        super(gif_menu, self).__init__()
        self.__app = app

        mi_exit = wx.MenuItem(self, wx.NewIdRef(), 'Exit')
        self.Bind(wx.EVT_MENU, self.OnExit, mi_exit)
        self.Append(mi_exit)
    
    def OnExit(self, event):
        """
        Executed when selecting "Exit".
        """
        wx.PostEvent(
            self.__app.frame.GetEventHandler(),
            wx.PyCommandEvent(
                wx.EVT_CLOSE.typeId, 
                self.__app.frame.GetId()
            )
        )