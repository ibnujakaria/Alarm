from PySide import QtGui
import os

class SystemTrayIcon(QtGui.QSystemTrayIcon):

    def __init__(self, parent):
        super(SystemTrayIcon, self).__init__(parent)
        self.prepareUi()
        self.prepareMenu()

    def prepareUi(self):
        icon = QtGui.QIcon('assets/ic_alarm_white_24dp_1x.png')
        self.setIcon(icon)
        self.setToolTip(self.parent().penampilWaktu.getStringOfWaktu(self.parent().getMode()))
        pass

    def prepareMenu(self):
        menu = QtGui.QMenu(self.parent())
        menu.addAction("Open", self.actionOpen)
        menu.addAction("Add Alarm", self.actionAddAlarm)
        menu.addAction("Setting", self.actionSetting)
        menu.addAction("Exit", self.actionExit)

        self.setContextMenu(menu)
        pass

    def actionExit(self):
        print("action exit")

        self.parent().live = False
        self.parent().close()

    def actionAddAlarm(self):
        print('action add alarm')

    def actionSetting(self):
        print('action setting')

    def actionOpen(self):
        print('action open')
        self.parent().show()

    def greet(self):
        self.showMessage("Alarm", "The alarm is now running on background",
                         QtGui.QSystemTrayIcon.Information, 10000)

        os.system("notify-send \"Alarm\" \"The alarm is now running on background\"")