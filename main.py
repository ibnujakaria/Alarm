import sys
from PySide import QtGui
from views import MainWindow

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()

    try:
        sys.exit(app.exec_())
    except (RuntimeError, InterruptedError, Exception, IOError):
        print("some errors occured")
        pass
