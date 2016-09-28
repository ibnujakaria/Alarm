from PySide import QtGui

class SettingDialog(QtGui.QDialog):

    def __init__(self, qWidget):
        super(SettingDialog, self).__init__(qWidget)

        self.prepareUi()

    def prepareUi(self):
        self.setWindowTitle("Setting")
        self.setFixedSize(300, 150)
        self.setModal(True)

        self.prepareButtons()
        self.prepareFooterButtons()

    def prepareButtons(self):
        self.labelFormatTime = QtGui.QLabel("Time Format", self)
        self.labelFormatTime.move(10, 13)

        self.comboFormatTime = QtGui.QComboBox(self)
        self.comboFormatTime.addItem('24 Hours')
        self.comboFormatTime.addItem('12 Hours')
        self.comboFormatTime.move(120, 10)

        if self.parent().getMode() is 1:
            self.comboFormatTime.setCurrentIndex(1)

    def prepareFooterButtons(self):
        self.buttonOk = QtGui.QPushButton("Apply", self)
        self.buttonOk.move(200, 110)
        self.buttonOk.clicked.connect(self.onButtonOkClicked)

        self.buttonCancel = QtGui.QPushButton("Cancel", self)
        self.buttonCancel.move(115, 110)
        self.buttonCancel.clicked.connect(self.onButtonCancelClicked)

    def onButtonOkClicked(self):
        mode = 0
        if self.comboFormatTime.currentText() == '12 Hours':
            mode = 1

        self.parent().setMode(mode)
        self.accept()
        pass

    def onButtonCancelClicked(self):
        print("cancel")
        self.reject()
        pass

    def getValue(self):
        amOrPm = None

        if  self.parent().getMode() is 1:
            amOrPm = self.comboAmPm.currentText()

        return self.comboHour.currentText(), self.comboMinute.currentText(), amOrPm

