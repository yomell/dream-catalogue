import sqlite3
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie, QKeySequence
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QApplication, QHeaderView, QDialog, QShortcut

from help import Ui_HelpWindow

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

db = QSqlDatabase.addDatabase('QSQLITE')
db.setDatabaseName('bookbase.sqlite')
db.open()


class Ui_Error(object):
    def setupUi(self, Error):
        Error.setObjectName("Error")
        Error.setFixedSize(211, 129)
        Error.setWindowFlag(QtCore.Qt.MSWindowsFixedSizeDialogHint)
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
        self.err_reason.setText(_translate("Error", ""))


class Ui_AddBook(object):
    def setupUi(self, AddBook):
        AddBook.setObjectName("AddBook")
        AddBook.setFixedSize(287, 289)
        AddBook.setWindowFlag(QtCore.Qt.MSWindowsFixedSizeDialogHint)
        font = QtGui.QFont()
        font.setFamily("Manrope")
        AddBook.setFont(font)
        self.enter_title = QtWidgets.QLineEdit(AddBook)
        self.enter_title.setGeometry(QtCore.QRect(150, 20, 113, 20))
        self.enter_title.setObjectName("enter_title")

        self.enter_writer = QtWidgets.QLineEdit(AddBook)
        self.enter_writer.setGeometry(QtCore.QRect(150, 60, 113, 20))
        self.enter_writer.setObjectName("enter_writer")

        self.enter_publisher = QtWidgets.QLineEdit(AddBook)
        self.enter_publisher.setGeometry(QtCore.QRect(150, 100, 113, 20))
        self.enter_publisher.setObjectName("enter_publisher")

        self.enter_lang = QtWidgets.QLineEdit(AddBook)
        self.enter_lang.setGeometry(QtCore.QRect(150, 140, 113, 20))
        self.enter_lang.setObjectName("enter_lang")

        self.enter_genre = QtWidgets.QLineEdit(AddBook)
        self.enter_genre.setGeometry(QtCore.QRect(150, 180, 113, 20))
        self.enter_genre.setObjectName("enter_genre")

        self.confirm_btn = QtWidgets.QPushButton(AddBook)
        self.confirm_btn.setGeometry(QtCore.QRect(90, 230, 101, 31))
        self.confirm_btn.clicked.connect(self.add_confirmation)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AddBook.setWindowIcon(icon)
        font = QtGui.QFont()
        font.setFamily("Manrope")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.confirm_btn.setFont(font)
        self.confirm_btn.setStyleSheet("QPushButton {\n"
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
        self.confirm_btn.setObjectName("confirm_btn")
        self.label_title = QtWidgets.QLabel(AddBook)
        self.label_title.setGeometry(QtCore.QRect(20, 20, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Manrope")
        font.setPointSize(11)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.label_writer = QtWidgets.QLabel(AddBook)
        self.label_writer.setGeometry(QtCore.QRect(20, 60, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Manrope")
        font.setPointSize(11)
        self.label_writer.setFont(font)
        self.label_writer.setObjectName("label_writer")
        self.label_publisher = QtWidgets.QLabel(AddBook)
        self.label_publisher.setGeometry(QtCore.QRect(20, 100, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Manrope")
        font.setPointSize(11)
        self.label_publisher.setFont(font)
        self.label_publisher.setObjectName("label_publisher")
        self.label_lang = QtWidgets.QLabel(AddBook)
        self.label_lang.setGeometry(QtCore.QRect(20, 140, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Manrope")
        font.setPointSize(11)
        self.label_lang.setFont(font)
        self.label_lang.setObjectName("label_lang")
        self.label_genre = QtWidgets.QLabel(AddBook)
        self.label_genre.setGeometry(QtCore.QRect(20, 180, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Manrope")
        font.setPointSize(11)
        self.label_genre.setFont(font)
        self.label_genre.setObjectName("label_genre")

        self.retranslateUi(AddBook)
        QtCore.QMetaObject.connectSlotsByName(AddBook)

    def retranslateUi(self, AddBook):
        _translate = QtCore.QCoreApplication.translate
        AddBook.setWindowTitle(_translate("AddBook", "Добавление книги"))
        self.confirm_btn.setText(_translate("AddBook", "Подтвердить"))
        self.label_title.setText(_translate("AddBook", "Название"))
        self.label_writer.setText(_translate("AddBook", "Автор"))
        self.label_publisher.setText(_translate("AddBook", "Издатель"))
        self.label_lang.setText(_translate("AddBook", "Язык"))
        self.label_genre.setText(_translate("AddBook", "Жанр"))

    def add_confirmation(self):
        con = sqlite3.connect("bookbase.sqlite")
        cur = con.cursor()

        entered = [" ".join([i.lower().capitalize() for i in self.enter_writer.text().split()]),
                   self.enter_title.text().lower().capitalize(),
                   self.enter_publisher.text().lower().capitalize(),
                   self.enter_lang.text().lower().capitalize(),
                   self.enter_genre.text().lower().capitalize()]

        if '' in entered:
            # Проверка на отстутсвие незаполненных строчек
            err = QDialog()
            err_ui = Ui_Error()
            err_ui.setupUi(err)
            err_ui.err_reason.setText(" Есть пустые строки")
            err.exec_()

        else:
            if entered[0] not in [k for i in cur.execute(f"SELECT name FROM writer").fetchall() for k in i]:
                # Проверка на наличие имени писателя в таблице писателей
                # Индекс беру чтобы не загромождать код тем, что есть в списке entered

                cur.execute(f"INSERT INTO writer(name) VALUES(?)", (entered[0],))
                # Если писателя нет, то мы его добавляем

            if entered[4] not in [k for i in cur.execute("SELECT title FROM genre") for k in i]:
                cur.execute(f"""INSERT INTO genre(title) VALUES('{entered[4]}')""")
            # Проверка на существование указанного жанра. Если его нет - мы добавляем его в таблицу
            # с жанрами
            # Я не сделал такую штуку, чтобы жанры разбивались на разные и добавлялись отдельно,
            # когда человек вводит их через пробел/запятую и т. д., не вижу в этом особой необходимости
            # (единственный случай, когда это имеет место - это когда человек вводит условно "роман фэнтези"
            # и "роман, фэнтези", потому что для этих жанров будет создана новая строчка в таблице жанров.
            # Впрочем, не так страшно

            vals = [list(i) for i in
                    cur.execute(f"""SELECT Автор, Название, Издатель, Язык, Жанр FROM book""").fetchall()]

            # for i in range(len(vals)):
            #     for k in range(len(vals[i])):
            #         if isinstance(vals[i][k], str):
            #             if i != 0:
            #                 vals[i][k] = vals[i][k].lower().capitalize()
            #             else:
            #                 vals[i][k] = " ".join([i.lower().capitalize() for i in self.enter_writer.text().split()])
            # Вроде этот код не несет смысла, но я оставлю на крайняк

            if entered not in vals:

                # Проверка на дубликат (я отказался от проверки только по автору и названию потому,
                # что есть люди, собирающие книги одного автора разных издательств / разных языков).
                # Проверка на жанр не особо логичная, ведь книга одного автора не может быть разных жанров, но это
                # сделано для избежания цикла, в котором не будет выделяться строка таблицы без жанра.
                # Ничего страшного в полной проверке дубликатов

                cur.execute(f"""INSERT INTO book(Автор, Название, Издатель, Язык, Жанр)
                         VALUES('{entered[0]}', '{entered[1]}',
                          '{entered[2]}', '{entered[3]}',
                          '{entered[4]}')""")
                # Добавляем в таблицу книг саму книгу и всё, что с ней связано
                # UPD 20.11.21: перевёл колонки таблицы "Book" на русский, потому что
                # композиция не будет соблюдаться, если в таблице колонки будут на английском

            else:
                err = QDialog()
                err_ui = Ui_Error()
                err_ui.setupUi(err)
                err_ui.err_reason.setText("Такая книга уже есть")
                err.exec_()

            con.commit()
            # Применяем изменения в БД

            catalogue.add_book_window.close()
            # Закрываем окно. Я забыл про переменную при запуске прогргаммы :)


class Ui_RemoveBook(object):
    def setupUi(self, RemoveBook):
        RemoveBook.setObjectName("RemoveBook")
        RemoveBook.setFixedSize(287, 114)
        RemoveBook.setWindowFlag(QtCore.Qt.MSWindowsFixedSizeDialogHint)
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

        self.rm_confirm_btn.clicked.connect(self.remove_confirmation)

        self.retranslateUi(RemoveBook)
        QtCore.QMetaObject.connectSlotsByName(RemoveBook)

    def retranslateUi(self, RemoveBook):
        _translate = QtCore.QCoreApplication.translate
        RemoveBook.setWindowTitle(_translate("RemoveBook", "Удаление книги"))
        self.rm_confirm_btn.setText(_translate("RemoveBook", "Подтвердить"))
        self.rm_label_title.setText(_translate("RemoveBook", "ID книги"))

    def remove_confirmation(self):
        con = sqlite3.connect("bookbase.sqlite")
        cur = con.cursor()

        if self.rm_enter_title.text() == '' or int(self.rm_enter_title.text()) not in \
                [k for i in cur.execute(f"SELECT [ID книги] FROM book").fetchall() for k in i]:
            err = QDialog()
            err_ui = Ui_Error()
            err_ui.setupUi(err)
            err_ui.err_reason.setText("Книги с таким ID нет")
            err.exec_()
            # Меню ошибки в случае указания ID, которого нет в таблице
        else:
            if len(cur.execute(f"""SELECT * FROM book 
            WHERE Жанр=(SELECT Жанр FROM book WHERE     
            [ID книги] = '{self.rm_enter_title.text()}')""").fetchall()) == 1:
                cur.execute(f"""DELETE FROM genre WHERE title=(SELECT Жанр FROM book WHERE
                [ID книги] = '{self.rm_enter_title.text()}')""")

            if len(cur.execute(f"""SELECT * FROM writer WHERE name=(SELECT Автор FROM book WHERE
            [ID книги] = '{self.rm_enter_title.text()}')""").fetchall()) == 1:
                cur.execute(f"""DELETE FROM writer WHERE name=(SELECT Автор FROM book WHERE
                [ID книги] = '{self.rm_enter_title.text()}')""")

            cur.execute(f"""DELETE FROM book WHERE [ID книги] = '{self.rm_enter_title.text()}'""")
            rows = [i + 1 for i in range(len(cur.execute("SELECT * FROM book").fetchall()))]
            bookids = [k for i in cur.execute("SELECT [ID книги] FROM book").fetchall() for k in i]
            for i in range(len(rows)):
                cur.execute(f"""UPDATE book SET [ID книги] = {rows[i]} WHERE [ID книги] = '{bookids[i]}'""")
                # Это сделано для подгона ID книги под ID строчки (чтоб все красиво было, и у второй книги
                # не было ID 13)
            cur.execute(f"""UPDATE sqlite_sequence
            SET seq = (SELECT MAX(rowid) FROM book)""")
            # Это сделано для того, что автоинкремент не шалил и принимал значение на 1 больше последнего ID книги
            con.commit()
            catalogue.remove_book_window.close()

class Ui_EvaX(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(640, 496)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.yandere = QMovie('dev.gif')
        self.label = QtWidgets.QLabel(Form)
        self.label.setMovie(self.yandere)
        self.label.setScaledContents(True)
        self.label.setGeometry(QtCore.QRect(0, 0, 640, 496))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "OMG ALEX??????"))



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(900, 700)
        MainWindow.setWindowFlag(QtCore.Qt.MSWindowsFixedSizeDialogHint)
        # Флаг, убирающий стрелочку от краев окна (чтоб нельзя было попытаться растянуть приложение)
        font = QtGui.QFont()
        font.setFamily("Manrope")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        font = QtGui.QFont()
        font.setFamily("Manrope")
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.db_view = QtWidgets.QTableView(self.centralwidget)
        self.db_view.setGeometry(QtCore.QRect(280, 10, 601, 571))
        font = QtGui.QFont()
        font.setFamily("HelveticaNeueCyr")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.db_view.setFont(font)
        self.db_view.setStyleSheet("""QTableView {
        border-radius: 25px;
        border: 2px solid grey;
        padding: 7px;
        width: 200px;
        height: 150px;
        selection-background-color: qlineargradient(x1: 0, y1: 0, x2: 0.5, y2: 0.5, stop: 0 #99FFCC, stop: 1 #99FFCC);
        selection-color: black;
            }""")
        self.db_view.setSortingEnabled(False)
        self.db_view.setObjectName("db_view")
        self.db_view.verticalHeader().setVisible(False)
        # Убираем колонки с номерами строк
        self.db_view.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        # Убираем возможность редактировать данные в таблице
        self.add_book = QtWidgets.QPushButton(self.centralwidget)
        self.add_book.setGeometry(QtCore.QRect(320, 600, 131, 41))
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
        self.remove_book.setGeometry(QtCore.QRect(710, 600, 131, 41))
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
        self.dropdown_list.setGeometry(QtCore.QRect(30, 80, 171, 26))
        self.dropdown_list.setObjectName("dropdown_list")
        font = QtGui.QFont("Manrope", 10)
        font.setBold(True)
        self.dropdown_list.setFont(font)

        self.column_names = ["Автор", "Название", "Издатель", "Язык", "Жанр", "ID книги"]
        for i in self.column_names:
            self.dropdown_list.addItem(i)

        self.order_list = QtWidgets.QComboBox(self.centralwidget)
        self.order_list.setGeometry(QtCore.QRect(30, 220, 171, 26))
        self.order_list.setObjectName("dropdown_list")
        font = QtGui.QFont("Manrope", 10)
        font.setBold(True)
        self.order_list.setFont(font)
        for i in ["По возрастанию", "По убыванию"]:
            self.order_list.addItem(i)

        self.label_filter = QtWidgets.QLabel(self.centralwidget)
        self.label_filter.setGeometry(QtCore.QRect(23, 20, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Manrope")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.label_filter.setFont(font)
        self.label_filter.setObjectName("label_filter")
        self.label_order = QtWidgets.QLabel(self.centralwidget)
        self.label_order.setGeometry(QtCore.QRect(48, 160, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Manrope")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.label_order.setFont(font)
        self.label_order.setObjectName("label_order")
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
        self.filter_confirm_btn.clicked.connect(self.filter_confirmation)
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

        self.Help_action.triggered.connect(MainWindow.help)
        self.add_book.clicked.connect(MainWindow.add_book_func)
        self.remove_book.clicked.connect(MainWindow.remove_book_func)

        self.Help.addAction(self.Help_action)
        self.menubar.addAction(self.Help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DREAM CATALOGUE"))
        self.add_book.setText(_translate("MainWindow", "Добавить книгу"))
        self.remove_book.setText(_translate("MainWindow", "Удалить книгу"))
        self.Help.setTitle(_translate("MainWindow", "Поддержка"))
        self.action_3.setText(_translate("MainWindow", "Поддержка"))
        self.Help_action.setText(_translate("MainWindow", "Поддержка"))
        self.label_filter.setText(_translate("MainWindow", "Сортировка"))
        self.filter_confirm_btn.setText(_translate("MainWindow", "Применить"))
        self.label_order.setText(_translate("MainWindow", "Порядок"))

    def filter_confirmation(self):
        order = QtCore.Qt.AscendingOrder if self.order_list.currentText() == "По возрастанию" \
            else QtCore.Qt.DescendingOrder
        # Выбираем порядок (возрастание / убывание, зависит от нижнего ComboBox'а)
        self.db_view.sortByColumn(self.column_names.index(self.dropdown_list.currentText()), order)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow, Ui_AddBook, Ui_RemoveBook):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.model = QSqlTableModel(self, db)
        self.model.setTable('book')
        self.model.select()

        self.shortcum = QShortcut(QKeySequence('Ctrl+C'), self)
        self.shortcum.activated.connect(self.yandev)

        self.db_view.setModel(self.model)
        self.db_view.setFocusPolicy(QtCore.Qt.NoFocus)
        # Убираем пунктир при выделении ячейки
        self.db_view.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        # Растягивание колонок по ширине содержимого

    def help(self):
        help_window = QDialog()
        help_window_ui = Ui_HelpWindow()
        help_window_ui.setupUi(help_window)
        help_window.exec_()
        # В функции ниже я добавил self для того, чтобы использовать её в другом классе. Кнопка помощи,
        # кроме как для показа аэродинамики коровы, не используется, и других функций в ней нет

    def yandev(self):
        yandev_window = QDialog()
        yandev_window_ui = Ui_EvaX()
        yandev_window_ui.setupUi(yandev_window)
        yandev_window_ui.yandere.start()
        yandev_window.exec_()

    def add_book_func(self):
        self.add_book_window = QDialog()
        self.add_book_window_ui = Ui_AddBook()
        self.add_book_window_ui.setupUi(self.add_book_window)
        self.add_book_window.exec_()
        self.model.select()
        # Эта строка для обновления таблицы. Какой же бред [ДАННЫЕ УДАЛЕНЫ], часов десять впустую убил

    def remove_book_func(self):
        self.remove_book_window = QDialog()
        self.remove_book_window_ui = Ui_RemoveBook()
        self.remove_book_window_ui.setupUi(self.remove_book_window)
        self.remove_book_window.exec_()
        self.model.select()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    catalogue = MainWindow()
    catalogue.statusBar().setSizeGripEnabled(False)
    # Убираем точки справа снизу окна. Теперь точо никто не попытается растянуть приложение
    catalogue.show()
    sys.exit(app.exec())
