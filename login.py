from PyQt5 import QtCore, QtGui, QtWidgets
from admin_support import Ui_support
from databases_sqlite import admin_database
import sys
import assets


class Ui_login_page(object):
    def setupUi(self, login_page):
        login_page.setObjectName("login_page")
        login_page.resize(771, 534)
        login_page.setMouseTracking(True)
        login_page.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        login_page.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.widget_2 = QtWidgets.QWidget(login_page)
        self.widget_2.setGeometry(QtCore.QRect(0, 0, 771, 531))
        self.widget_2.setObjectName("widget_2")

        self.entry_holder = QtWidgets.QLabel(self.widget_2)
        self.entry_holder.setGeometry(QtCore.QRect(370, 80, 331, 371))
        self.entry_holder.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border: 2px solid rgb(234, 196, 163);\n"
                                        "border-radius: 50px;")
        self.entry_holder.setText("")
        self.entry_holder.setObjectName("entry_holder")

        self.title_card = QtWidgets.QLabel(self.widget_2)
        self.title_card.setGeometry(QtCore.QRect(80, 40, 341, 451))
        self.title_card.setStyleSheet("background-color: rgb(234, 196, 163);\n"
                                      "border-image: url(:/newPrefix/assets/Add_a_subheading-removebg-preview-removebg-preview.png);\n"
                                      "border: 2px;\n"
                                      "border-radius: 25px;")
        self.title_card.setText("")
        self.title_card.setObjectName("title_card")

        self.logo = QtWidgets.QLabel(self.widget_2)
        self.logo.setGeometry(QtCore.QRect(90, 90, 311, 221))
        self.logo.setStyleSheet("image: url(:/newPrefix/assets/logo.png);")
        self.logo.setText("")
        self.logo.setObjectName("logo")

        self.tapsilog_meaning = QtWidgets.QLabel(self.widget_2)
        self.tapsilog_meaning.setGeometry(QtCore.QRect(90, 310, 321, 16))
        self.tapsilog_meaning.setStyleSheet("font: 6pt \"Rockwell\";\n"
                                            "")
        self.tapsilog_meaning.setObjectName("tapsilog_meaning")

        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(430, 90, 251, 111))
        self.label.setStyleSheet("font: 15pt \"Arial Black\";")
        self.label.setObjectName("label")

        self.username_entry = QtWidgets.QLineEdit(self.widget_2)
        self.username_entry.setGeometry(QtCore.QRect(430, 200, 241, 41))
        self.username_entry.setAutoFillBackground(False)
        self.username_entry.setStyleSheet("border: 2px;\n"
                                          "border-bottom: 2px solid black;")
        self.username_entry.setClearButtonEnabled(False)
        self.username_entry.setObjectName("username_entry")

        self.password_entry = QtWidgets.QLineEdit(self.widget_2)
        self.password_entry.setGeometry(QtCore.QRect(430, 260, 241, 41))
        self.password_entry.setAutoFillBackground(False)
        self.password_entry.setStyleSheet("border: 2px;\n"
                                          "border-bottom: 2px solid black;")
        self.password_entry.setClearButtonEnabled(False)
        self.password_entry.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_entry.setObjectName("password_entry")

        self.log_in_button = QtWidgets.QPushButton(self.widget_2)
        self.log_in_button.clicked.connect(self.login_pressed)
        self.log_in_button.setGeometry(QtCore.QRect(460, 320, 181, 41))
        self.log_in_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.log_in_button.setMouseTracking(True)
        self.log_in_button.setStyleSheet("QPushButton#log_in_button{\n"
                                         "    border: 3px solid black;\n"
                                         "    border-radius: 10px;\n"
                                         "    font: 87 10pt \"Arial Black\";\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton#log_in_button:hover{\n"
                                         "    background-color: rgb(234, 196, 163)\n"
                                         "}")
        self.log_in_button.setDefault(True)
        self.log_in_button.setObjectName("log_in_button")

        self.exit_button = QtWidgets.QPushButton(self.widget_2)
        self.exit_button.clicked.connect(self.close_pressed)
        self.exit_button.setGeometry(QtCore.QRect(740, 0, 31, 28))
        self.exit_button.setStyleSheet("QPushButton#exit_button{\n"
                                       "    font: 8pt \"Wide Latin\";\n"
                                       "    color: rgb(0, 0, 0);\n"
                                       "    background-color:rgb(255, 255, 255);\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton#exit_button:hover{\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "    background-color: rgb(255, 0, 0)\n"
                                       "}\n"
                                       "\n"
                                       "")
        self.exit_button.setObjectName("exit_button")

        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(470, 370, 101, 31))
        self.label_2.setObjectName("label_2")

        self.forgot_button = QtWidgets.QPushButton(self.widget_2)
        self.forgot_button.clicked.connect(self.run_support)
        self.forgot_button.setGeometry(QtCore.QRect(560, 370, 91, 31))
        self.forgot_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.forgot_button.setStyleSheet("QPushButton#forgot_button{\n"
                                         "    font: 8pt \"Segoe UI Variable Small\";\n"
                                         "    border: 2px;\n"
                                         "    color: rgb(234, 196, 163);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton#forgot_button:hover{\n"
                                         "    font: 8pt \"Segoe UI Variable Small\";\n"
                                         "    text-decoration: underline;\n"
                                         "}\n"
                                         "\n"
                                         "")
        self.forgot_button.setObjectName("forgot_button")

        self.see_pass = QtWidgets.QPushButton(self.widget_2)
        self.see_pass.clicked.connect(self.see_password)
        self.see_pass.setCheckable(True)
        self.see_pass.setGeometry(QtCore.QRect(630, 260, 41, 41))
        self.see_pass.setMouseTracking(True)
        self.see_pass.setStyleSheet("QPushButton#see_pass{\n"
                                    "    border: 2px;\n"
                                    "    image: url(:/newPrefix/assets/unsee.png);\n"
                                    "}\n"
                                    "")

        self.see_pass.setText("")
        self.see_pass.setObjectName("see_pass")

        self.bdsm_logo = QtWidgets.QLabel(self.widget_2)
        self.bdsm_logo.setGeometry(QtCore.QRect(50, 30, 121, 101))
        self.bdsm_logo.setStyleSheet("image: url(:/newPrefix/assets/logo_main.png);")
        self.bdsm_logo.setText("")
        self.bdsm_logo.setObjectName("bdsm_logo")

        self.retranslateUi(login_page)
        QtCore.QMetaObject.connectSlotsByName(login_page)

    def retranslateUi(self, login_page):
        _translate = QtCore.QCoreApplication.translate
        login_page.setWindowTitle(_translate("login_page", "Form"))
        self.tapsilog_meaning.setText(
            _translate("login_page", "Total Activity Processed through a Strictly Implemented Log System "))
        self.label.setText(_translate("login_page", "SECURITY LOGIN"))
        self.username_entry.setPlaceholderText(_translate("login_page", "Username"))
        self.password_entry.setPlaceholderText(_translate("login_page", "Password"))
        self.log_in_button.setText(_translate("login_page", "LOGIN"))
        self.exit_button.setText(_translate("login_page", "X"))
        self.label_2.setText(_translate("login_page", "Forgot password?"))
        self.forgot_button.setText(_translate("login_page", "Click here"))

    def login_pressed(self):
        self.databaseConnect = admin_database.AdminDatabase()
        if self.username_entry.text() == "" or self.password_entry.text() == "":
            self.messagebox_input_fields()
        else:
            try:
                if self.username_entry.text() == ((self.databaseConnect.search_admin(self.username_entry.text()))[0]) and self.password_entry.text() == (
                        (self.databaseConnect.search_admin(self.username_entry.text()))[1]):
                    print("Log IN")
            except TypeError:
                print("NAh")

    def close_pressed(self):
        sys.exit(app.exec_())

    def see_password(self, checked):
        if checked == False:
            self.see_pass.setStyleSheet("QPushButton#see_pass{\n"
                                        "    border: 2px;\n"
                                        "    image: url(:/newPrefix/assets/see.png);\n"
                                        "}\n"
                                        "")
            self.password_entry.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.see_pass.setStyleSheet("QPushButton#see_pass{\n"
                                        "    border: 2px;\n"
                                        "    image: url(:/newPrefix/assets/unsee.png);\n"
                                        "}\n"
                                        "")
            self.password_entry.setEchoMode(QtWidgets.QLineEdit.Password)

    def run_support(self):
        self.support = QtWidgets.QDialog()
        self.run = Ui_support()
        self.run.setupUi(self.support)
        self.support.show()

    def messagebox_input_fields(self):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/assets/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.box = QtWidgets.QMessageBox()
        self.box.setWindowIcon(icon)
        self.box.setIcon(QtWidgets.QMessageBox.Information)
        self.box.setWindowTitle("INFO: 001")
        self.box.setText("All Fields needs input to proceed.")
        self.box.show()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    login_page = QtWidgets.QWidget()
    ui = Ui_login_page()
    ui.setupUi(login_page)
    login_page.show()
    sys.exit(app.exec_())
