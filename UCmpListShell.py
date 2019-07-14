class TCompetitor():
    def __init__(self):
        self.name = 'unnamed'

class TCmpListShell():
    def __init__(self):
        self.onChange = None
        self.list = []

    def append(self, item):
        self.list.append(item)
        self.__doChange()

    def delete(self, index):
        del self.list[index]
        self.__doChange()

    def __doChange(self):
        if self.onChange is not None:
            self.onChange()        
