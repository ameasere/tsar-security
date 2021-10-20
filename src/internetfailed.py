# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'InternetFailed.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_FailedScreen(object):
    def setupUi(self, FailedScreen):
        if not FailedScreen.objectName():
            FailedScreen.setObjectName(u"FailedScreen")
        FailedScreen.resize(680, 400)
        icon = QIcon()
        icon.addFile(u"iconfile.ico", QSize(), QIcon.Normal, QIcon.Off)
        FailedScreen.setWindowIcon(icon)
        self.centralwidget = QWidget(FailedScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.dropShadowFrame = QFrame(self.centralwidget)
        self.dropShadowFrame.setObjectName(u"dropShadowFrame")
        self.dropShadowFrame.setStyleSheet(u"QFrame {	\n"
"	background-color: rgba(255, 255, 255, .15);\n"
"}")
        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)
        self.title = QLabel(self.dropShadowFrame)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(0, 0, 661, 61))
        font = QFont()
        font.setFamily(u"Consolas")
        font.setPointSize(40)
        self.title.setFont(font)
        self.title.setStyleSheet(u"color: rgb(3, 198, 252);\n"
"background-color: rgba(255, 255, 255, 0); ")
        self.title.setAlignment(Qt.AlignCenter)
        self.subtitle = QLabel(self.dropShadowFrame)
        self.subtitle.setObjectName(u"subtitle")
        self.subtitle.setGeometry(QRect(0, 90, 661, 141))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(14)
        self.subtitle.setFont(font1)
        self.subtitle.setStyleSheet(u"color: rgba(239, 0, 156, 255);\n"
"background-color: rgba(255, 255, 255, 0); ")
        self.subtitle.setAlignment(Qt.AlignCenter)
        self.credit = QLabel(self.dropShadowFrame)
        self.credit.setObjectName(u"credit")
        self.credit.setGeometry(QRect(20, 350, 621, 21))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(10)
        self.credit.setFont(font2)
        self.credit.setStyleSheet(u"color: rgba(239, 0, 156, 255);\n"
"background-color: rgba(255, 255, 255, 0); ")
        self.credit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.exitButton = QPushButton(self.dropShadowFrame)
        self.exitButton.setObjectName(u"exitButton")
        self.exitButton.setGeometry(QRect(280, 270, 75, 23))
        self.exitButton.setStyleSheet(u"color: rgba(255, 255, 255, 255);\n"
"background-color: rgba(239, 0, 156, 255);")

        self.verticalLayout.addWidget(self.dropShadowFrame)

        FailedScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(FailedScreen)

        QMetaObject.connectSlotsByName(FailedScreen)
    # setupUi

    def retranslateUi(self, FailedScreen):
        FailedScreen.setWindowTitle(QCoreApplication.translate("FailedScreen", u"Tsar", None))
        self.title.setText(QCoreApplication.translate("FailedScreen", u"<html><head/><body><p><span style=\" font-weight:600;\">Internet Failed</span></p></body></html>", None))
        self.subtitle.setText(QCoreApplication.translate("FailedScreen", u"<html><head/><body><p>You are seeing this message because Tsar failed to detect</p><p>a viable internet connection to interface with the central</p><p>server. As such, Tsar cannot function. Please re-open Tsar</p><p>when your internet connection is available.</p></body></html>", None))
        self.credit.setText(QCoreApplication.translate("FailedScreen", u"<strong>Created</strong>: enigmapr0ject", None))
        self.exitButton.setText(QCoreApplication.translate("FailedScreen", u"Exit", None))
    # retranslateUi

