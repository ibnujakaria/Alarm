from PySide import QtGui, QtCore
import threading, time, simpleaudio as SimpleAudio

class SurpriseDialog(QtGui.QDialog):

    opened = False
    vibrator = QtCore.Signal()
    speedX = 5
    leftAsli = 0
    soundObj = None

    def __init__(self, parent):
        super(SurpriseDialog, self).__init__(parent)

        self.setWindowTitle("BOOOM!!")
        self.setFixedSize(300, 150)
        self.setModal(False)

        self.finished.connect(self.onDialogClose)
        self.vibrator.connect(self.vibrate)

        self.soundObj = SimpleAudio.WaveObject.from_wave_file('assets/sounds/alarm.wav')

    def boom(self):
        if (self.opened is not True):
            self.opened = True
            self.show()
            self.leftAsli = self.frameGeometry().left()
            self.playObj = self.soundObj.play()

        thread = threading.Thread(target = self.doVibrating)
        try:
            thread.start()
        except:
            pass

    def onDialogClose(self):
        self.opened = False # make it false again so the next alarm could open this dialog
        # send the signal to prevent the current alarm to show this box
        self.parent().dismissed.emit()
        self.playObj.stop()

    def doVibrating(self):
        while self.opened is True:
            self.vibrator.emit()
            self.speedX = -self.speedX
            time.sleep(0.3)

    def vibrate(self):
        self.move(self.leftAsli + self.speedX, self.frameGeometry().top())