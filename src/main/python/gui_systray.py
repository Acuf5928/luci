import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets

import sys


class SystemTrayIcon(QtWidgets.QSystemTrayIcon):
    def __init__(self, ctx):
        super(SystemTrayIcon, self).__init__()
        self.ctx = ctx
        self.menu = QtWidgets.QMenu()
        #self.activated.connect(self.iconActivated)
        self.setIcon(QtGui.QIcon(self.ctx.icon()))
        self.setMenu()

    # Init sysTray
    def setMenu(self):
        self.menu.clear()

        self.on = self.menu.addAction("ON")
        self.on.triggered.connect(self.setON)

        self.off = self.menu.addAction("OFF")
        self.off.triggered.connect(self.setOFF)

        self.auto = self.menu.addAction("AUTO")
        self.auto.triggered.connect(self.setAUTO)

        exitAction = self.menu.addAction("Exit")
        exitAction.triggered.connect(self.exit)

        self.setContextMenu(self.menu)

    # Set functions of all menu elements, from here:
    def setAUTO(self):
        self.ctx.serial().write(2)

    def setON(self):
        self.ctx.serial().write(1)

    def setOFF(self):
        self.ctx.serial().write(0)

    def exit(self):
        sys.exit()

    # To here


# Start gui_sysTray
def main(appctxt):
    trayIcon = SystemTrayIcon(appctxt)
    trayIcon.show()
    exit_code = appctxt.app.exec_()
    sys.exit(exit_code)