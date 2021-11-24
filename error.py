class Ui_Error(object):
    def setupUi(self, Error):
        Error.setObjectName("Error")
        Error.resize(211, 129)
        font = QtGui.QFont()
        font.setFamily("HelveticaNeueCyr")
        Error.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Error.setWindowIcon(icon)
        self.err_notification = QtWidgets.QLabel(Error)
        self.err_notification.setGeometry(QtCore.QRect(40, 10, 131, 31))
        font = QtGui.QFont()
        font.setFamily("HelveticaNeueCyr")
        font.setPointSize(22)
        self.err_notification.setFont(font)
        self.err_notification.setObjectName("err_notification")
        self.err_reason = QtWidgets.QLabel(Error)
        self.err_reason.setGeometry(QtCore.QRect(10, 50, 191, 41))
        font = QtGui.QFont()
        font.setFamily("HelveticaNeueCyr")
        font.setPointSize(14)
        self.err_reason.setFont(font)
        self.err_reason.setObjectName("err_reason")

        self.retranslateUi(Error)
        QtCore.QMetaObject.connectSlotsByName(Error)

    def retranslateUi(self, Error):
        _translate = QtCore.QCoreApplication.translate
        Error.setWindowTitle(_translate("Error", "Ошибка"))
        self.err_notification.setText(_translate("Error", "ОШИБКА"))
        self.err_reason.setText(_translate("Error", "Книги с таким ID нет"))
