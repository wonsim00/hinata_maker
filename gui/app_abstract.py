import wx

class gif_app_abstract(wx.App):
    def __init__(self, **kwargs):
        super(gif_app_abstract, self).__init__(**kwargs)
        self._keep_going = True

    def frame(self):
        raise NotImplementedError

    def task_bar_icon(self):
        raise NotImplementedError

    def end_main_loop(self):
        self._keep_going = False