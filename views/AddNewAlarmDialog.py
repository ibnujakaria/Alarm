from PySide import QtGui

class AddNewAlarmDialog(QtGui.QDialog):

    def __init__(self, parent):
        super(AddNewAlarmDialog, self).__init__(parent)

        self.prepareUi()

    def prepareUi(self):
        self.setWindowTitle("Add new alarm")
        self.setFixedSize(300, 150)
        self.setModal(True)

        self.prepareInputText()
        self.prepareFooterButtons()

    def prepareInputText(self):
        self.comboHour = QtGui.QComboBox(self)
        self.comboHour.resize(60, 40)
        self.comboHour.move(50, 40)
        self.labelHour = QtGui.QLabel("Hour", self)
        self.labelHour.move(50, 15)
        self.labelHour.resize(self.labelHour.sizeHint())

        self.comboMinute = QtGui.QComboBox(self)
        self.comboMinute.resize(60, 40)
        self.comboMinute.move(120, 40)
        self.labelMinute = QtGui.QLabel("Minute", self)
        self.labelMinute.move(120, 15)
        self.labelMinute.resize(self.labelMinute.sizeHint())

        self.comboAmPm = QtGui.QComboBox(self)
        self.comboAmPm.resize(60, 40)
        self.comboAmPm.move(190, 40)
        self.comboAmPm.addItems(['AM', 'PM'])
        self.comboAmPm.setDisabled(not bool(self.parent().mode))
        self.labelAmPm = QtGui.QLabel("AM/PM", self)
        self.labelAmPm.move(190, 15)
        self.labelAmPm.resize(self.labelAmPm.sizeHint())

        for i in range(1, 60):
            if  i < 10:
                i = "0" + str(i)

            if int(i) < 24:
                self.comboHour.addItem(str(i), int(i))

            self.comboMinute.addItem(str(i), int(i))

        self.comboHour.setCurrentIndex(self.parent().penampilWaktu.getHour() - 1)
        self.comboMinute.setCurrentIndex(self.parent().penampilWaktu.getMinute() - 1)


    def prepareFooterButtons(self):
        self.buttonOk = QtGui.QPushButton("Set Alarm", self)
        self.buttonOk.move(200, 110)
        self.buttonOk.clicked.connect(self.onButtonOkClicked)

        self.buttonCancel = QtGui.QPushButton("Cancel", self)
        self.buttonCancel.move(115, 110)
        self.buttonCancel.clicked.connect(self.onButtonCancelClicked)

    def onButtonOkClicked(self):
        print("ok")
        self.accept()
        pass

    def onButtonCancelClicked(self):
        print("cancel")
        self.reject()
        pass

    def getValue(self):
        return self.comboHour.currentText(), self.comboMinute.currentText(), self.comboAmPm.currentText()