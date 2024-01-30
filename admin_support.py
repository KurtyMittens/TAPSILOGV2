from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import assets

class Ui_support(object):
    def setupUi(self, support):
        support.setObjectName("support")
        support.setWindowModality(QtCore.Qt.NonModal)
        support.resize(630, 420)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/assets/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        support.setWindowIcon(icon)
        self.title_card = QtWidgets.QLabel(support)
        self.title_card.setGeometry(QtCore.QRect(0, 0, 631, 421))
        self.title_card.setStyleSheet("background-color: rgb(234, 196, 163);\n"
"border-image: url(:/newPrefix/assets/Add_a_subheading-removebg-preview-removebg-preview.png);\n"
"")
        self.title_card.setText("")
        self.title_card.setObjectName("title_card")
        self.bdsm_logo = QtWidgets.QLabel(support)
        self.bdsm_logo.setGeometry(QtCore.QRect(-10, 0, 131, 121))
        self.bdsm_logo.setStyleSheet("image: url(:/newPrefix/assets/logo_main.png)")
        self.bdsm_logo.setText("")
        self.bdsm_logo.setObjectName("bdsm_logo")
        self.tapsilog_logo = QtWidgets.QLabel(support)
        self.tapsilog_logo.setGeometry(QtCore.QRect(520, 10, 81, 91))
        self.tapsilog_logo.setStyleSheet("image: url(:/newPrefix/assets/logo.png)")
        self.tapsilog_logo.setText("")
        self.tapsilog_logo.setObjectName("tapsilog_logo")
        self.admi_supp_label = QtWidgets.QLabel(support)
        self.admi_supp_label.setGeometry(QtCore.QRect(110, 60, 401, 51))
        self.admi_supp_label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.admi_supp_label.setAcceptDrops(False)
        self.admi_supp_label.setStyleSheet("font: 25pt \"Arial Black\";")
        self.admi_supp_label.setObjectName("admi_supp_label")
        self.admin_pass_but = QtWidgets.QPushButton(support)
        self.admin_pass_but.setEnabled(True)
        self.admin_pass_but.setGeometry(QtCore.QRect(150, 140, 321, 51))
        self.admin_pass_but.setStyleSheet("border: 2px solid black;\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"background-color: rgb(244, 232, 226);\n"
"border-radius: 10px;\n"
"")
        self.admin_pass_but.setObjectName("admin_pass_but")
        self.admin_code_but = QtWidgets.QPushButton(support)
        self.admin_code_but.setEnabled(True)
        self.admin_code_but.setGeometry(QtCore.QRect(150, 220, 321, 51))
        self.admin_code_but.setStyleSheet("border: 2px solid black;\n"
"background-color: rgb(244, 232, 226);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius: 10px;\n"
"")
        self.admin_code_but.setObjectName("admin_code_but")

        self.retranslateUi(support)
        QtCore.QMetaObject.connectSlotsByName(support)

    def retranslateUi(self, support):
        _translate = QtCore.QCoreApplication.translate
        support.setWindowTitle(_translate("support", "Admin Support"))
        self.admi_supp_label.setToolTip(_translate("support", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.admi_supp_label.setWhatsThis(_translate("support", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.admi_supp_label.setText(_translate("support", "ADMIN SUPPORT"))
        self.admin_pass_but.setText(_translate("support", "I FORGOT MY ADMIN PASSWORD"))
        self.admin_code_but.setText(_translate("support", "RETRIEVE MY ADMIN CODE"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    support = QtWidgets.QDialog()
    ui = Ui_support()
    ui.setupUi(support)
    support.show()
    sys.exit(app.exec_())
