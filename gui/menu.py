import wx

from .app_abstract import gif_app_abstract

class gif_menu(wx.Menu):
    """
    Defines wx.Menu object for gif_task_bar_icon.
    """

    def __init__(self, app: gif_app_abstract):
        super(gif_menu, self).__init__()
        self.__app = app
        
        schedule_index = {}
        for idx, scheduler in enumerate(app.animation.get_schedulers()):
            mi_swap = wx.MenuItem(self, wx.NewIdRef(), scheduler.menu_name)
            schedule_index[mi_swap.Id] = idx
            self.Bind(wx.EVT_MENU, self.OnSwap, mi_swap)
            self.Append(mi_swap)
        self.__schedule_index = schedule_index

        mi_exit = wx.MenuItem(self, wx.NewIdRef(), 'Exit')
        self.Bind(wx.EVT_MENU, self.OnExit, mi_exit)
        self.Append(mi_exit)
    
    def OnSwap(self, event):
        self.__app.animation.set_curr_scheduler(
            self.__schedule_index[event.Id])

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