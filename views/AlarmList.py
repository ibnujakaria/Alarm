from PySide import QtGui

class AlarmList:

    currentActiveAlarmIndex = 0

    def __init__(self, qWidget):
        self.qWidget = qWidget
        self.prepareData()

    def prepareData(self):
        self.listAlarms = []
        self.listLabelAlarms = []
        self.listButtonDismissAlarms = []
        self.listButtonRemoveAlarms = []
        self.emptyLabel = QtGui.QLabel("There is no alarm.", self.qWidget)
        self.emptyLabel.setVisible(False)
        self.emptyLabel.move(10, 110)
        self.icons = {
            'alarmOff': QtGui.QIcon("assets/ic_volume_off_black_24dp_1x.png"),
            'alarmOn': QtGui.QIcon("assets/ic_volume_up_black_24dp_1x.png"),
            'remove': QtGui.QIcon("assets/ic_delete_black_24dp_1x.png"),
        }

    def addNewAlarm(self, hour, minute, mode = None):
        print("mode -> " + str(mode))
        if len(self.listAlarms) == 3:
            return

        if mode == "PM":
            hour = str(int(hour) + 12)
            print("hour -> " + hour)

        alarm = {
            'hour': hour,
            'minute': minute,
            'dismissed': False
        }

        self.listAlarms.append(alarm)

        # ubah ke belakang lagi
        if mode == "PM":
            hour = str(int(hour) - 12)

        if mode == None:
            mode = ""

        newLabel = QtGui.QLabel(str(hour) + ":" + str(minute) + " " + mode, self.qWidget)
        newLabel.move(10, 113 + (30 * (len(self.listAlarms) - 1)))
        newLabel.show()
        self.listLabelAlarms.append(newLabel)

        newDismissButton = QtGui.QPushButton('', self.qWidget)
        newDismissButton.setIcon(self.icons.get('alarmOn'));
        newDismissButton.move(100, 110 + (30 * (len(self.listAlarms) - 1)))
        newDismissButton.alarm = alarm
        newDismissButton.clicked.connect(lambda: self.toggleAlarm(alarm, newDismissButton))
        newDismissButton.show()
        self.listButtonDismissAlarms.append(newDismissButton)

        newRemoveButton = QtGui.QPushButton('', self.qWidget)
        newRemoveButton.setIcon(self.icons.get('remove'));
        newRemoveButton.move(140, 110 + (30 * (len(self.listAlarms) - 1)))
        newRemoveButton.alarm = alarm
        newRemoveButton.show()
        self.listButtonRemoveAlarms.append(newRemoveButton)

        print("new alarm added")
        self.displayList() # this will update the list displayed

    def displayList(self):
        if len(self.listAlarms) < 1:
            self.emptyLabel.setVisible(True)
        else:
            self.emptyLabel.setVisible(False)

        # self.qWidget.repaint()

    def updateLabelDoToTheFormatChange(self, mode):
        for i in range(len(self.listAlarms)):
            alarm = self.listAlarms[i]
            label = self.listLabelAlarms[i]
            hour = alarm.get('hour')
            minute = alarm.get('minute')
            amOrPm = ""

            if mode is 1 and int(hour) >= 12:
                hour = str(int(hour) - 12)
                amOrPm = "PM"
            elif mode is 1 and int(hour) < 12:
                amOrPm = "AM"

            label.setText(str(hour) + ":" + str(minute) + " " + amOrPm)
            label.resize(label.sizeHint())

    def setCurrentActiveAlarmIndex(self, index):
        self.currentActiveAlarmIndex = index

    def getCurrentActiveAlarmIndex(self):
        return self.currentActiveAlarmIndex

    def toggleAlarm(self, alarm, button):
        if alarm.get('dismissed') is False:
            button.setIcon(self.icons.get('alarmOff'))
            self.dismissAlarm(self.listAlarms.index(alarm))
        else:
            button.setIcon(self.icons.get('alarmOn'))
            self.setAlarmOn(self.listAlarms.index(alarm))

    def dismissAlarm(self, index = None):
        if index is None:
            self.listAlarms[self.getCurrentActiveAlarmIndex()].update({'dismissed': True})
            self.listButtonDismissAlarms[self.getCurrentActiveAlarmIndex()].setIcon(self.icons.get('alarmOff'))
        else:
            self.listAlarms[index].update({'dismissed': True})

    def setAlarmOn(self, index = None):
            self.listAlarms[index].update({'dismissed': False})