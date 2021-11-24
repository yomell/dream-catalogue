class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("Manrope")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Manrope")
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.db_view = QtWidgets.QTableView(self.centralwidget)
        self.db_view.setGeometry(QtCore.QRect(260, 10, 501, 471))
        font = QtGui.QFont()
        font.setFamily("HelveticaNeueCyr")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.db_view.setFont(font)
        self.db_view.setStyleSheet("QTableView {\n"
                                   "    selection-background-color: qlineargradient(x1: 0, y1: 0, x2: 0.5, y2: 0.5,\n"
                                   "                                stop: 0 #FF92BB, stop: 1 purple);\n"
                                   "}")
        self.db_view.setSortingEnabled(False)
        self.db_view.setObjectName("db_view")
        self.add_book = QtWidgets.QPushButton(self.centralwidget)
        self.add_book.setGeometry(QtCore.QRect(300, 500, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Manrope")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.add_book.setFont(font)
        self.add_book.setStyleSheet("QPushButton {\n"
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
                                    "\n"
                                    "QPushButton:default {\n"
                                    "    border-color: navy; /* make the default button prominent */\n"
                                    "}")
        self.add_book.setObjectName("add_book")
        self.remove_book = QtWidgets.QPushButton(self.centralwidget)
        self.remove_book.setGeometry(QtCore.QRect(590, 500, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Manrope")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.remove_book.setFont(font)
        self.remove_book.setStyleSheet("QPushButton {\n"
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
                                       "\n"
                                       "QPushButton:default {\n"
                                       "    border-color: navy; /* make the default button prominent */\n"
                                       "}")
        self.remove_book.setObjectName("remove_book")
        self.dropdown_list = QtWidgets.QComboBox(self.centralwidget)
        self.dropdown_list.setGeometry(QtCore.QRect(30, 80, 171, 21))
        self.dropdown_list.setObjectName("dropdown_list")
        self.label_filter = QtWidgets.QLabel(self.centralwidget)
        self.label_filter.setGeometry(QtCore.QRect(60, 20, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Manrope")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.label_filter.setFont(font)
        self.label_filter.setObjectName("label_filter")
        self.filter_confirm_btn = QtWidgets.QPushButton(self.centralwidget)
        self.filter_confirm_btn.setGeometry(QtCore.QRect(70, 120, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Manrope")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.filter_confirm_btn.setFont(font)
        self.filter_confirm_btn.setStyleSheet("QPushButton {\n"
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
                                              "\n"
                                              "QPushButton:default {\n"
                                              "    border-color: navy; /* make the default button prominent */\n"
                                              "}")
        self.filter_confirm_btn.setObjectName("filter_confirm_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        font = QtGui.QFont()
        font.setFamily("Manrope")
        font.setBold(True)
        font.setWeight(75)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.Help = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("Manrope")
        font.setBold(True)
        font.setWeight(75)
        self.Help.setFont(font)
        self.Help.setObjectName("Help")
        MainWindow.setMenuBar(self.menubar)
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.Help_action = QtWidgets.QAction(MainWindow)
        self.Help_action.setEnabled(True)
        self.Help_action.setObjectName("Help_action")
        self.Help.addAction(self.Help_action)
        self.menubar.addAction(self.Help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.add_book.setText(_translate("MainWindow", "Добавить книгу"))
        self.remove_book.setText(_translate("MainWindow", "Удалить книгу"))
        self.label_filter.setText(_translate("MainWindow", "Фильтр"))
        self.filter_confirm_btn.setText(_translate("MainWindow", "Применить"))
        self.Help.setTitle(_translate("MainWindow", "Поддержка"))
        self.action_3.setText(_translate("MainWindow", "Поддержка"))
        self.Help_action.setText(_translate("MainWindow", "Поддержка"))
