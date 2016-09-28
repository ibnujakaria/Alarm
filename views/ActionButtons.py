from PySide import QtGui, QtCore
from .AddNewAlarmDialog import AddNewAlarmDialog
from .SettingDialog import SettingDialog

class ActionButtons():

    def __init__(self, qWidget):
        self.qWidget = qWidget
        self.alarm = False
        self.prepareDependencies()

    def prepareDependencies(self):
        self.icons = {
            'alarmOff': QtGui.QIcon("assets/ic_alarm_off_black_24dp_1x.png"),
            'alarmOn': QtGui.QIcon("assets/ic_alarm_on_black_24dp_1x.png"),
            'alarmAdd': QtGui.QIcon("assets/ic_alarm_add_black_24dp_1x.png"),
            'settings': QtGui.QIcon("assets/ic_settings_black_24dp_1x.png")
        }

    def show(self):
        # self.btnIndicator = QtGui.QPushButton("", self.qWidget)
        # self.btnIndicator.move(350, 110)
        # self.btnIndicator.clicked.connect(self.qWidget.toggleAlarm)

        self.btnAddAlarm = QtGui.QPushButton(self.icons.get('alarmAdd'), "", self.qWidget)
        self.btnAddAlarm.move(350, 130)
        self.btnAddAlarm.setToolTip("Add a new alarm")
        self.btnAddAlarm.clicked.connect(self.qWidget.addNewAlarm)
        self.toggleAlarm()

        self.btnSetting = QtGui.QPushButton("", self.qWidget)
        self.btnSetting.move(350, 162)
        self.btnSetting.clicked.connect(self.qWidget.openSettingDialog)
        self.btnSetting.setIcon(self.icons.get('settings'))


    def toggleAlarm(self):
        return
        if self.alarm is not True:
            self.btnIndicator.setIcon(self.icons.get('alarmOff'))
            self.btnIndicator.setToolTip("Alarm is not active")
            self.alarm = True
        else:
            self.btnIndicator.setIcon(self.icons.get('alarmOn'))
            self.btnIndicator.setToolTip("Alarm is active")
            self.alarm = False


    def addNewAlarm(self):
        addAlarmDialog = AddNewAlarmDialog(self.qWidget)
        addAlarmDialog.exec_()

        if addAlarmDialog.result():
            value = addAlarmDialog.getValue()
            self.qWidget.alarmList.addNewAlarm(value[0], value[1], value[2])

    def openSettingDialog(self):
        settingDialog = SettingDialog(self.qWidget)
        settingDialog.exec_()