# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 650)
        MainWindow.setMinimumSize(QtCore.QSize(400, 650))
        MainWindow.setMaximumSize(QtCore.QSize(400, 650))
        MainWindow.setIconSize(QtCore.QSize(32, 32))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.villager_image = QtWidgets.QLabel(parent=self.centralwidget)
        self.villager_image.setGeometry(QtCore.QRect(70, 20, 256, 256))
        self.villager_image.setMinimumSize(QtCore.QSize(256, 256))
        self.villager_image.setMaximumSize(QtCore.QSize(256, 256))
        self.villager_image.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.villager_image.setWordWrap(True)
        self.villager_image.setOpenExternalLinks(True)
        self.villager_image.setObjectName("villager_image")
        self.name_menu = QtWidgets.QComboBox(parent=self.centralwidget)
        self.name_menu.setGeometry(QtCore.QRect(130, 570, 151, 26))
        self.name_menu.setObjectName("name_menue")
        self.name_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.name_label.setGeometry(QtCore.QRect(60, 330, 121, 31))
        self.name_label.setWordWrap(True)
        self.name_label.setObjectName("name_label")
        self.gender_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.gender_label.setGeometry(QtCore.QRect(60, 410, 121, 31))
        self.gender_label.setWordWrap(True)
        self.gender_label.setObjectName("gender_label")
        self.personality_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.personality_label.setGeometry(QtCore.QRect(60, 490, 121, 41))
        self.personality_label.setWordWrap(True)
        self.personality_label.setObjectName("personality_label")
        self.hobby_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.hobby_label.setGeometry(QtCore.QRect(230, 360, 121, 31))
        self.hobby_label.setWordWrap(True)
        self.hobby_label.setObjectName("hobby_label")
        self.birthday_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.birthday_label.setGeometry(QtCore.QRect(230, 440, 121, 31))
        self.birthday_label.setWordWrap(True)
        self.birthday_label.setObjectName("birthday_label")
        self.error_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.error_label.setGeometry(QtCore.QRect(100, 290, 200, 31))
        self.error_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.error_label.setWordWrap(True)
        self.error_label.setObjectName("error_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.villager_image.setText(_translate("MainWindow", "TextLabel"))
        self.name_label.setText(_translate("MainWindow", "TextLabel"))
        self.gender_label.setText(_translate("MainWindow", "TextLabel"))
        self.personality_label.setText(_translate("MainWindow", "TextLabel"))
        self.hobby_label.setText(_translate("MainWindow", "TextLabel"))
        self.birthday_label.setText(_translate("MainWindow", "TextLabel"))
        self.error_label.setText(_translate("MainWindow", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
