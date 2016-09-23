from PySide import QtGui


class SurpriseDialog(QtGui.QDialog):

    opened = False

    def __init__(self, parent):
        super(SurpriseDialog, self).__init__(parent)

        self.setWindowTitle("BOOOM!!")
        self.setFixedSize(300, 150)
        self.setModal(True)

    def boom(self):
        if (self.opened is not True):
            self.opened = True
            self.exec_()