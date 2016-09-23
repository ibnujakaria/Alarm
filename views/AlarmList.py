from PySide import QtGui

class AlarmList:

    def __init__(self, qWidget):
        self.qWidget = qWidget
        self.prepareData()

    def prepareData(self):
        self.listAlarms = []
        self.listLabelAlarms = []
        self.emptyLabel = QtGui.QLabel("There is no alarm.", self.qWidget)
        self.emptyLabel.setVisible(False)
        self.emptyLabel.move(10, 110)

    def addNewAlarm(self, hour, minute, mode = None):
        if len(self.listAlarms) == 3:
            return

        self.listAlarms.append({
            'hour': hour,
            'minute': minute
        })

        newLabel = QtGui.QLabel(str(hour) + ":" + str(minute), self.qWidget)
        newLabel.move(10, 110 + (20 * (len(self.listAlarms) - 1)))
        newLabel.show()
        self.listLabelAlarms.append(newLabel)

        print("new alarm added")
        self.displayList() # this will update the list displayed

    def displayList(self):
        if len(self.listAlarms) < 1:
            self.emptyLabel.setVisible(True)
        else:
            self.emptyLabel.setVisible(False)

        # self.qWidget.repaint()