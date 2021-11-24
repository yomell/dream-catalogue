from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HelpWindow(object):
    def setupUi(self, Help_Window):
        Help_Window.setObjectName("Help_Window")
        Help_Window.resize(604, 503)
        self.cow_aer_label = QtWidgets.QLabel(Help_Window)
        self.cow_aer_label.setGeometry(QtCore.QRect(20, 420, 561, 71))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Help_Window.setWindowIcon(icon)
        font = QtGui.QFont()
        font.setFamily("Manrope")
        self.cow_aer_label.setFont(font)
        self.cow_aer_label.setObjectName("cow_aer_label")
        self.cow_aer = QtWidgets.QLabel(Help_Window)
        self.cow_aer.setGeometry(QtCore.QRect(50, 20, 604, 391))
        self.cow_aer.setText("")
        self.cow_aer.setPixmap(QtGui.QPixmap("venv/cow.png"))
        self.cow_aer.setObjectName("cow_aer")

        self.retranslateUi(Help_Window)
        QtCore.QMetaObject.connectSlotsByName(Help_Window)

    def retranslateUi(self, Help_Window):
        _translate = QtCore.QCoreApplication.translate
        Help_Window.setWindowTitle(_translate("Help_Window", "0 ПОМОЩИ"))
        self.cow_aer_label.setText(_translate("Help_Window",
                                              "<html><head/><body><p align=\"center\"><span style=\" "
                                              "font-size:36pt;\">Аэродинамика коровы</span></p></body></html>"))
