import PIL
from PIL import Image
from PIL import ImageTk
import tkinter as tk

class TLeftSideFrame():
    def __init__(self, parent, cmpLstShell):       
        self.subject = tk.Frame(parent, bg = 'white', width = 300)
        self.subject.pack_propagate(0)
        self.cmpLstShell = cmpLstShell

        self.lstbxCompetitors = tk.Listbox(self.subject)       
        self.lstbxCompetitors.pack()
                         
        self.btnDeleteCompetitor = tk.Button(
            self.subject,
            text = "Удалить конкурента",
            command = self.__btnDeleteCompetitorClick
            )       
        self.btnDeleteCompetitor.pack()

        self.update()
        
    def update(self):
        self.lstbxCompetitors.delete(0, tk.END)
        for cmp in self.cmpLstShell.list:
            self.lstbxCompetitors.insert(tk.END, cmp.name)

    def __btnDeleteCompetitorClick(self):
        # <code here>
        pass


    
