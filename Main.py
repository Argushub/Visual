import PIL
from PIL import Image
from PIL import ImageTk
import tkinter as tk

import ULeftFrame
import UMap
import UCmpListShell

class TMainWindow():
    def __init__(self):
        self.subject = tk.Tk()
        self.subject.geometry("800x600")
        self.subject.state('zoomed')
        
        # cmpLst = competitors list
        self.cmpLstShell = UCmpListShell.TCmpListShell()
        # <<< сюда вставить загрузку БД из файла
        self.cmpLstShell.onChange = self.__update
        
        self.frmLeft = ULeftFrame.TLeftSideFrame(self.subject, self.cmpLstShell)
        self.frmLeft.subject.pack(side = tk.LEFT, fill = tk.Y)

        self.imgMap = UMap.TMap(self.subject, self.cmpLstShell)
        self.imgMap.subject.pack(side = tk.RIGHT, fill = tk.Y)

    def __update(self):
        self.frmLeft.update()
        self.imgMap.update()

wndMain = TMainWindow()
wndMain.subject.mainloop()

