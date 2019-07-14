import tkinter as tk

MR_OK = 0
MR_CANCEL = 1

class TModalResult():
    def __init__(self):
        self.result = -1


class TInputFrame():
    def __init__(self, parent):       
        self.subject = tk.Frame(parent, bg = 'white', width = 250, height = 50)
        self.subject.pack_propagate(0)

        self.__legend = tk.StringVar()
        self.__labLegend = tk.Label(
            self.subject,
            textvariable = self.__legend,
            width = 10
            )
        self.__labLegend.pack(side = tk.LEFT)  
        
        self.__txtField = tk.Text(
            self.subject,
            height = 1,
            width = 30,
            )       
        self.__txtField.pack(side = tk.LEFT)       

    @property
    def text(self):
        return self.__txtField.get("1.0", tk.END)

    @text.setter
    def text(self, value):
        self.__txtField.delete(1.0, tk.END)
        self.__txtField.insert(tk.END, value)

    @property
    def legend(self):
        return self.__legend.get()

    @legend.setter
    def legend(self, value):
        self.__legend.set(value)   
