import sys
from PySide import QtGui
from views import MainWindow

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()

    sys.exit(app.exec_())