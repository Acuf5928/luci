import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets

import code_helper as helper


class App(QtWidgets.QMainWindow):

    def __init__(self, ctx):
        super().__init__()

        self.ctx = ctx

        self.setWindowIcon(QtGui.QIcon(ctx.icon()))
        self.setMinimumSize(QtCore.QSize(500, 130))
        self.setMaximumSize(QtCore.QSize(500, 130))

        self.initUI()

    # Init Ui
    def initUI(self):
        self.setWindowTitle(self.ctx.name())

        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.move(165, 10)
        self.comboBox.resize(325, 30)
        self.comboBox.addItems(self.ctx.serial().listDevice())

        self.textbox1 = QtWidgets.QCheckBox(self)
        self.textbox1.move(165, 50)
        self.textbox1.resize(325, 30)

        self.textbox2 = QtWidgets.QCheckBox(self)
        self.textbox2.move(165, 90)
        self.textbox2.resize(325, 30)

        self.text = QtWidgets.QLabel('Serial port:', self)
        self.text.move(10, 10)
        self.text.resize(130, 30)

        self.text1 = QtWidgets.QLabel('Set ON on connect:', self)
        self.text1.move(10, 50)
        self.text1.resize(130, 30)

        self.text2 = QtWidgets.QLabel('Auto on connect:', self)
        self.text2.move(10, 90)
        self.text2.resize(130, 30)

    # Prevent program exit when clik on X button
    def closeEvent(self, event):
        self.hide()
        event.ignore()
