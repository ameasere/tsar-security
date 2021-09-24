# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'apikey.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import assets_rc

class Ui_apiwindow(object):
    def setupUi(self, apiwindow):
        if not apiwindow.objectName():
            apiwindow.setObjectName(u"apiwindow")
        apiwindow.resize(680, 399)
        icon = QIcon()
        icon.addFile(u"iconfile.ico", QSize(), QIcon.Normal, QIcon.Off)
        apiwindow.setWindowIcon(icon)
        self.centralwidget = QWidget(apiwindow)
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
        self.label_title = QLabel(self.dropShadowFrame)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(-10, -10, 91, 61))
        font = QFont()
        font.setFamily(u"Consolas")
        font.setPointSize(40)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"color: rgb(3, 198, 252);\n"
"background-color: rgba(255, 255, 255, 0); ")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_credits = QLabel(self.dropShadowFrame)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setGeometry(QRect(460, 0, 201, 41))
        self.label_credits.setFont(font)
        self.label_credits.setStyleSheet(u"color: rgba(239, 0, 156, 255);\n"
"background-color: rgba(255, 255, 255, 0); ")
        self.label_credits.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.apibox = QLineEdit(self.dropShadowFrame)
        self.apibox.setObjectName(u"apibox")
        self.apibox.setGeometry(QRect(10, 90, 391, 20))
        self.label_credits_2 = QLabel(self.dropShadowFrame)
        self.label_credits_2.setObjectName(u"label_credits_2")
        self.label_credits_2.setGeometry(QRect(10, 50, 131, 21))
        font1 = QFont()
        font1.setFamily(u"Consolas")
        font1.setPointSize(10)
        self.label_credits_2.setFont(font1)
        self.label_credits_2.setStyleSheet(u"color: rgba(239, 0, 156, 255);\n"
"background-color: rgba(255, 255, 255, 0); ")
        self.label_credits_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_credits_3 = QLabel(self.dropShadowFrame)
        self.label_credits_3.setObjectName(u"label_credits_3")
        self.label_credits_3.setGeometry(QRect(230, 10, 141, 21))
        self.label_credits_3.setFont(font1)
        self.label_credits_3.setStyleSheet(u"color: rgba(239, 0, 156, 255);\n"
"background-color: rgba(255, 255, 255, 0); ")
        self.label_credits_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.writekey = QPushButton(self.dropShadowFrame)
        self.writekey.setObjectName(u"writekey")
        self.writekey.setGeometry(QRect(10, 120, 75, 23))
        font2 = QFont()
        font2.setFamily(u"Consolas")
        self.writekey.setFont(font2)
        self.writekey.setStyleSheet(u"color: rgba(255, 255, 255, 255);\n"
"background-color: rgba(239, 0, 156, 255);")
        self.changelog_3 = QLabel(self.dropShadowFrame)
        self.changelog_3.setObjectName(u"changelog_3")
        self.changelog_3.setGeometry(QRect(410, 50, 241, 231))
        font3 = QFont()
        font3.setFamily(u"Consolas")
        font3.setPointSize(20)
        self.changelog_3.setFont(font3)
        self.changelog_3.setStyleSheet(u"color: rgb(3, 198, 252);\n"
"background-color: rgba(255, 255, 255, 0); ")
        self.changelog_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.exitButton = QPushButton(self.dropShadowFrame)
        self.exitButton.setObjectName(u"exitButton")
        self.exitButton.setGeometry(QRect(100, 120, 75, 23))
        self.exitButton.setFont(font2)
        self.exitButton.setStyleSheet(u"color: rgba(255, 255, 255, 255);\n"
"background-color: rgba(239, 0, 156, 255);")
        self.response = QLabel(self.dropShadowFrame)
        self.response.setObjectName(u"response")
        self.response.setGeometry(QRect(10, 170, 401, 71))
        self.response.setFont(font1)
        self.response.setStyleSheet(u"color: rgb(3, 198, 252);\n"
"background-color: rgba(255, 255, 255, 0); ")
        self.response.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_title_2 = QLabel(self.dropShadowFrame)
        self.label_title_2.setObjectName(u"label_title_2")
        self.label_title_2.setGeometry(QRect(70, -10, 91, 61))
        self.label_title_2.setFont(font)
        self.label_title_2.setStyleSheet(u"color: rgb(3, 198, 252);\n"
"background-color: rgba(255, 255, 255, 0); ")
        self.label_title_2.setAlignment(Qt.AlignCenter)
        self.label1 = QLabel(self.dropShadowFrame)
        self.label1.setObjectName(u"label1")
        self.label1.setGeometry(QRect(0, 270, 651, 101))
        self.label1.setFont(font1)
        self.label1.setStyleSheet(u"color: rgb(3, 198, 252);\n"
"background-color: rgba(255, 255, 255, 0); ")
        self.label1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.dropShadowFrame)

        apiwindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(apiwindow)

        QMetaObject.connectSlotsByName(apiwindow)
    # setupUi

    def retranslateUi(self, apiwindow):
        apiwindow.setWindowTitle(QCoreApplication.translate("apiwindow", u"Tsar Beta 1", None))
        self.label_title.setText(QCoreApplication.translate("apiwindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Tsar</span></p></body></html>", None))
        self.label_credits.setText(QCoreApplication.translate("apiwindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Created</span><span style=\" font-size:12pt;\">: enigmapr0ject</span></p></body></html>", None))
        self.label_credits_2.setText(QCoreApplication.translate("apiwindow", u"<html><head/><body><p>Enter API key here</p></body></html>", None))
        self.label_credits_3.setText(QCoreApplication.translate("apiwindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; font-style:italic;\">API Key</span></p></body></html>", None))
        self.writekey.setText(QCoreApplication.translate("apiwindow", u"Write Key", None))
        self.changelog_3.setText(QCoreApplication.translate("apiwindow", u"<html><head/><body><p><img src=\":/icon/iconfile.ico\"/></p></body></html>", None))
        self.exitButton.setText(QCoreApplication.translate("apiwindow", u"Close", None))
        self.response.setText(QCoreApplication.translate("apiwindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_title_2.setText(QCoreApplication.translate("apiwindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">BETA 1</span></p></body></html>", None))
        self.label1.setText(QCoreApplication.translate("apiwindow", u"<html><head/><body><p>If your API key is not exactly how it is shown on your</p><p>beta testing portal, the server will refuse you access to the</p><p>application. Please make sure your API key here appears the</p><p>same as on https://enigmapr0ject.live/tsar</p></body></html>", None))
    # retranslateUi

