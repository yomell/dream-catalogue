import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableView, QHeaderView, QDialog
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel

from help import Ui_HelpWindow

db = QSqlDatabase.addDatabase('QSQLITE')
db.setDatabaseName('bookbase.sqlite')
db.open()


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
        self.db_view.setGeometry(QtCore.QRect(280, 70, 471, 381))
        self.db_view.setObjectName("db_view")

        self.add_book = QtWidgets.QPushButton(self.centralwidget)
        self.add_book.setGeometry(QtCore.QRect(30, 90, 111, 31))
        self.add_book.setObjectName("add_book")
        self.add_book.clicked.connect(self.add_book_window)

        self.remove_book = QtWidgets.QPushButton(self.centralwidget)
        self.remove_book.setGeometry(QtCore.QRect(30, 130, 111, 31))
        self.remove_book.setObjectName("remove_book")

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

        self.Help_action.triggered.connect(self.help_window)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.model = QSqlTableModel(self, db)
        self.model.setTable('book')
        self.model.select()

        self.db_view.setModel(self.model)
        self.db_view.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        # Растягивание колонок по ширине содержимого

    def add_book_window(self):
        add_book_window.exec_()

    def help_window(self):
        help_window.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.add_book.setText(_translate("MainWindow", "Добавить книгу"))
        self.remove_book.setText(_translate("MainWindow", "Удалить книгу"))
        self.Help.setTitle(_translate("MainWindow", "Поддержка"))
        self.action_3.setText(_translate("MainWindow", "Поддержка"))
        self.Help_action.setText(_translate("MainWindow", "Поддержка"))


class Ui_add_book(object):
    def setupUi(self, add_book):
        add_book.setObjectName("add_book")
        add_book.resize(282, 237)
        add_book.setFont(QtGui.QFont('Manrope', 10))
        self.enter_title = QtWidgets.QLineEdit(add_book)
        self.enter_title.setGeometry(QtCore.QRect(150, 20, 113, 20))
        self.enter_title.setObjectName("enter_name")

        self.enter_writer = QtWidgets.QLineEdit(add_book)
        self.enter_writer.setGeometry(QtCore.QRect(150, 60, 113, 20))
        self.enter_writer.setObjectName("enter_writerID")

        self.enter_publisher = QtWidgets.QLineEdit(add_book)
        self.enter_publisher.setGeometry(QtCore.QRect(150, 100, 113, 20))
        self.enter_publisher.setObjectName("enter_publisher")

        self.enter_lang = QtWidgets.QLineEdit(add_book)
        self.enter_lang.setGeometry(QtCore.QRect(150, 140, 113, 20))
        self.enter_lang.setObjectName("enter_lang")

        self.label_name = QtWidgets.QLabel(add_book)
        self.label_name.setGeometry(QtCore.QRect(20, 20, 81, 16))
        self.label_name.setObjectName("label_name")

        self.label_author = QtWidgets.QLabel(add_book)
        self.label_author.setGeometry(QtCore.QRect(20, 60, 81, 16))
        self.label_author.setObjectName("label_author")

        self.label_publisher = QtWidgets.QLabel(add_book)
        self.label_publisher.setGeometry(QtCore.QRect(20, 100, 81, 16))
        self.label_publisher.setObjectName("label_publisher")

        self.label_lang = QtWidgets.QLabel(add_book)
        self.label_lang.setGeometry(QtCore.QRect(20, 140, 81, 16))
        self.label_lang.setObjectName("label_lang")

        self.confirm_btn = QtWidgets.QPushButton(add_book)
        self.confirm_btn.setGeometry(QtCore.QRect(90, 190, 101, 31))
        self.confirm_btn.setObjectName("confirm_btn")
        self.confirm_btn.clicked.connect(self.confirmation)

        self.retranslateUi(add_book)
        QtCore.QMetaObject.connectSlotsByName(add_book)

    # ЗАВТРА!!! Сделать обновление таблицы после добавления элемента и автозакрытие после кнопки подтверждения
    def confirmation(self):
        con = sqlite3.connect("bookbase.sqlite")
        cur = con.cursor()
        if self.enter_writer not in cur.execute(f"SELECT name FROM writer").fetchall():
            # Проверка на наличие имени писателя в таблице писателей
            cur.execute(f"INSERT INTO writer(name) VALUES(?)", (self.enter_writer.text(),))
            # Если писателя нет, то мы его добавляем
        cur.execute(f"""INSERT INTO book(name, title, publisher, language)
         VALUES('{self.enter_writer.text()}', '{self.enter_title.text()}',
          '{self.enter_publisher.text()}', '{self.enter_lang.text()}')""")
        # Добавляем в таблицу книг саму книгу и всё, что с ней связано
        con.commit()
        # Применяем изменения в БД
        db.close()
        db.open()
        add_book_window.close()
        # Костыльный метод обновления таблицы

    def retranslateUi(self, add_book):
        _translate = QtCore.QCoreApplication.translate
        add_book.setWindowTitle(_translate("add_book", "Добавление книги"))
        self.confirm_btn.setText(_translate("add_book", "Подтвердить"))
        self.label_name.setText(_translate("add_book", "Название"))
        self.label_author.setText(_translate("add_book", "Автор"))
        self.label_publisher.setText(_translate("add_book", "Издатель"))
        self.label_lang.setText(_translate("add_book", "Язык"))


add_book_window = QDialog()
add_book_window_ui = Ui_add_book()
add_book_window_ui.setupUi(add_book_window)

help_window = QDialog()
help_window_ui = Ui_HelpWindow()
help_window_ui.setupUi(help_window)