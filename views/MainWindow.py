from PySide import QtGui, QtCore
from cores import MenampilkanWaktu, AngkaTerbilang
from .AlarmList import AlarmList
from .ActionButtons import ActionButtons
from .SurpriseDialog import SurpriseDialog
import threading, time

class MainWindow (QtGui.QWidget):

    bombed = QtCore.Signal()

    def __init__(self):
        super(MainWindow, self).__init__()

        self.live = True
        self.mode = 0 # 0 for 24 hours, and 1 for 12 hours
        self.prepareUI()

    def prepareUI(self):
        self.setWindowIcon(QtGui.QIcon("assets/ic_access_alarm_black_24dp_1x.png"))
        self.setFixedSize(400, 180)
        self.settingPosition()
        self.prepareDigitalClock()
        self.prepareButtons()
        self.prepareAlarmList()
        self.show()

        # surprise dialog
        self.surpriseDialog = SurpriseDialog(self)

        self.bombed.connect(self.boom)

        try:
            self.thread = threading.Thread(target=self.updateClock)
            self.thread.start()
        except:
            print("Some erros on thread.")

    def settingPosition(self):
        desktopGeometry = QtGui.QDesktopWidget().availableGeometry()
        myGeometry = self.frameGeometry()
        myGeometry.moveCenter(desktopGeometry.center())
        self.move(myGeometry.topLeft())

    def prepareDigitalClock(self):
        self.penampilWaktu = MenampilkanWaktu()

        # self.clockLabel = QtGui.QLabel(self.penampilWaktu.getWaktuBiasa(), self)
        self.clockLabel = QtGui.QLCDNumber(self)
        self.clockLabel.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.clockLabel.setDigitCount(8)
        self.clockLabel.display(self.penampilWaktu.getWaktuBiasa())
        self.clockLabel.resize(400, 100)

    def updateClock(self):
        while self.live:
            self.clockLabel.display(self.penampilWaktu.getWaktuBiasa())
            self.setToolTip(self.penampilWaktu.getStringOfWaktu())
            self.setWindowTitle("Alarm - " + self.penampilWaktu.getWaktuBiasa())

            # check if the alarm is coming
            self.checkTheAlarmIsComing()
            time.sleep(1)

        print("closing...")

    def checkTheAlarmIsComing(self):
        for alarm in self.alarmList.listAlarms:
            currentHour = self.penampilWaktu.getHour()
            currentMinute = self.penampilWaktu.getMinute()

            # print('alarm\t-> ' + alarm.get('hour'))
            # print('now\t\t-> ' + str(currentHour))
            # print('alarm\t-> ' + alarm.get('minute'))
            # print('now\t\t-> ' + str(currentMinute))

            if int(alarm.get('hour')) == int(currentHour) and int(alarm.get('minute')) == int(currentMinute):
                # QtCore.QObject.emit(self, QtCore.SIGNAL("alarm_on"))
                self.bombed.emit()

    def boom(self):
        self.surpriseDialog.boom()
        print("boombing")
        pass

    def prepareButtons(self):
        self.actionButton = ActionButtons(self)
        self.actionButton.show()

    def prepareAlarmList(self):
        self.alarmList = AlarmList(self)
        self.alarmList.displayList()

    def toggleAlarm(self):
        self.actionButton.toggleAlarm()

    def addNewAlarm(self):
        self.actionButton.addNewAlarm()

    def closeEvent(self, event):
        self.live = False