import wx

class gif_frame(wx.Frame):
    """
    Defines wx.Frame object (window)
    for displaying animated gif images.
    """

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
        """
        Executed when close event on gif_frame object is detected.
        It destroys the window and terminates the app.
        """
        self.__app.keep_going = False
        self.Destroy()
    
    def prepare(self, raw_images):
        """
        Prepares itself for displaying animated gif images.
        """
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
        """
        Sets the image to be shown at the next frame and its position.
        """
        self.SetShape(self.__regions[image_idx])
        self.SetPosition((x_pos, y_pos))
        self.__images[image_idx].Show()

        if self.__prev >= 0 and self.__prev != image_idx:
            self.__images[self.__prev].Hide()
        self.__prev = image_idx
        self.Show()