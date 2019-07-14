import PIL
from PIL import Image
from PIL import ImageTk
import tkinter as tk

import UCommonStuff

class TNewCompetitorWindow():
    def __init__(self, parent, newCmp, modalResult):
        self.subject = tk.Toplevel(parent, bg = 'white')
        self.subject.geometry("300x400")
        self.newCmp = newCmp
        self.modalResult = modalResult
        self.modalResult.result = UCommonStuff.MR_CANCEL

        self.inptName = UCommonStuff.TInputFrame(self.subject)
        self.inptName.legend = 'Название организации'
        self.inptName.text = ''
        self.inptName.subject.pack(side = tk.TOP)
               
        self.btnSubmit = tk.Button(
            self.subject,
            text = "Отправить",
            command = self.__btnSubmitClick
            )       
        self.btnSubmit.pack(side = tk.TOP)        
       
    def __btnSubmitClick(self):
        self.modalResult.result = UCommonStuff.MR_OK
        self.newCmp.name = self.inptName.text
        self.subject.destroy()
