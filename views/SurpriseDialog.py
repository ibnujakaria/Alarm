from PySide import QtGui


class SurpriseDialog(QtGui.QDialog):

    opened = False

    def __init__(self, parent):
        super(SurpriseDialog, self).__init__(parent)

        self.setWindowTitle("BOOOM!!")
        self.setFixedSize(300, 150)
        self.setModal(True)

        self.finished.connect(self.onDialogClose)

    def boom(self):
        if (self.opened is not True):
            self.opened = True
            self.exec_()

    def onDialogClose(self):
        self.opened = False # make it false again so the next alarm could open this dialog
        # send the signal to prevent the current alarm to show this box
        self.parent().dismissed.emit()

