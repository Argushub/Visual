import PIL
from PIL import Image
from PIL import ImageTk
import tkinter as tk

import UNewCompetitorWindow
import UCmpListShell
import UCommonStuff

class TMap():
    def __init__(self, parent, cmpLstShell):       
        self.parent = parent
        self.__PILimg = Image.open("theMap.gif")
        self.__TKimg = ImageTk.PhotoImage(self.__PILimg)
        self.subject = tk.Label(parent, image = self.__TKimg)
        self.subject.bind('<Button-1>', self.__mapClick)
        self.cmpLstShell = cmpLstShell

        self.update()
        
    def __mapClick(self, event):
        newCmp = UCmpListShell.TCompetitor()
        modalResult = UCommonStuff.TModalResult()
        wndNewCompetitor = UNewCompetitorWindow.TNewCompetitorWindow(self.parent, newCmp, modalResult)
        # убираем системные кнопки свернуть, расширить
        wndNewCompetitor.subject.transient(self.subject) 
        # передаем поток этому окну (делаем его модальным)
        wndNewCompetitor.subject.grab_set()  
        # фокусируем приложение на этом окне
        wndNewCompetitor.subject.focus_set()
        wndNewCompetitor.subject.wait_window()

        if modalResult.result == UCommonStuff.MR_OK:
            self.cmpLstShell.append(newCmp)
   
    def update(self):
        # <code here>
        pass
