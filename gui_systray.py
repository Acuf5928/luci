import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets

import sys
import _thread


class SystemTrayIcon(QtWidgets.QSystemTrayIcon):
    def __init__(self, icon, parent=None):
        QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)
        self.menu = QtWidgets.QMenu(parent)
        self.icon = icon
        self.setMenu()

    def setSerial(self, serial):
        self.serial = serial

    # Init sysTray
    def setMenu(self):
        self.menu.clear()

        self.on = self.menu.addAction("ON")
        self.on.triggered.connect(self.setON)

        self.off = self.menu.addAction("OFF")
        self.off.triggered.connect(self.setOFF)

        exitAction = self.menu.addAction("Exit")
        exitAction.triggered.connect(self.exit)

        self.setContextMenu(self.menu)

    # Set functions of all menu elements, from here:
    def setON(self):
        self.serial.write(1)

    def setOFF(self):
        self.serial.write(0)

    def exit(self):
        sys.exit()

    # To here


# Start gui_sysTray
def main(image, serial):
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    trayIcon = SystemTrayIcon(QtGui.QIcon(image), w)
    trayIcon.setSerial(serial)
    trayIcon.show()
    sys.exit(app.exec_())
