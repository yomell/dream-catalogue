class Ui_RemoveBook(object):
    def setupUi(self, RemoveBook):
        RemoveBook.setObjectName("RemoveBook")
        RemoveBook.resize(287, 114)
        font = QtGui.QFont()
        font.setFamily("Manrope")
        font.setPointSize(11)
        RemoveBook.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        RemoveBook.setWindowIcon(icon)
        self.rm_confirm_btn = QtWidgets.QPushButton(RemoveBook)
        self.rm_confirm_btn.setGeometry(QtCore.QRect(90, 70, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Manrope")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.rm_confirm_btn.setFont(font)
        self.rm_confirm_btn.setStyleSheet("QPushButton {\n"
                                          "    border: 2px solid #8f8f91;\n"
                                          "    border-radius: 6px;\n"
                                          "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                          "                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
                                          "    min-width: 80px;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:pressed {\n"
                                          "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                          "                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:flat {\n"
                                          "    border: none; /* no border for a flat push button */\n"
                                          "}\n"
                                          "")
        self.rm_confirm_btn.setObjectName("rm_confirm_btn")
        self.rm_enter_title = QtWidgets.QLineEdit(RemoveBook)
        self.rm_enter_title.setGeometry(QtCore.QRect(150, 30, 113, 20))
        self.rm_enter_title.setText("")
        self.rm_enter_title.setObjectName("rm_enter_title")
        self.rm_label_title = QtWidgets.QLabel(RemoveBook)
        self.rm_label_title.setGeometry(QtCore.QRect(20, 30, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Manrope")
        font.setPointSize(11)
        self.rm_label_title.setFont(font)
        self.rm_label_title.setObjectName("rm_label_title")

        self.retranslateUi(RemoveBook)
        QtCore.QMetaObject.connectSlotsByName(RemoveBook)

    def retranslateUi(self, RemoveBook):
        _translate = QtCore.QCoreApplication.translate
        RemoveBook.setWindowTitle(_translate("RemoveBook", "Удаление книги"))
        self.rm_confirm_btn.setText(_translate("RemoveBook", "Подтвердить"))
        self.rm_label_title.setText(_translate("RemoveBook", "ID книги"))
