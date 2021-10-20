# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainapp.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import assets_rc

class Ui_main(object):
    def setupUi(self, main):
        if not main.objectName():
            main.setObjectName(u"main")
        main.resize(680, 400)
        icon = QIcon()
        icon.addFile(u"iconfile.ico", QSize(), QIcon.Normal, QIcon.Off)
        main.setWindowIcon(icon)
        self.centralwidget = QWidget(main)
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
        self.userbox = QLineEdit(self.dropShadowFrame)
        self.userbox.setObjectName(u"userbox")
        self.userbox.setGeometry(QRect(230, 100, 161, 20))
        self.changelog = QLabel(self.dropShadowFrame)
        self.changelog.setObjectName(u"changelog")
        self.changelog.setGeometry(QRect(10, 50, 221, 201))
        font1 = QFont()
        font1.setFamily(u"Consolas")
        font1.setPointSize(20)
        self.changelog.setFont(font1)
        self.changelog.setStyleSheet(u"color: rgb(3, 198, 252);\n"
"background-color: rgba(255, 255, 255, 0); ")
        self.changelog.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.changelog_2 = QLabel(self.dropShadowFrame)
        self.changelog_2.setObjectName(u"changelog_2")
        self.changelog_2.setGeometry(QRect(10, 260, 221, 81))
        self.changelog_2.setFont(font1)
        self.changelog_2.setStyleSheet(u"color: rgba(239, 0, 156, 255);\n"
"background-color: rgba(255, 255, 255, 0); ")
        self.changelog_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.github = QPushButton(self.dropShadowFrame)
        self.github.setObjectName(u"github")
        self.github.setGeometry(QRect(10, 350, 75, 23))
        font2 = QFont()
        font2.setFamily(u"Consolas")
        self.github.setFont(font2)
        self.github.setStyleSheet(u"color: rgba(255, 255, 255, 255);\n"
"background-color: rgba(239, 0, 156, 255);")
        self.label_credits_2 = QLabel(self.dropShadowFrame)
        self.label_credits_2.setObjectName(u"label_credits_2")
        self.label_credits_2.setGeometry(QRect(230, 70, 141, 21))
        font3 = QFont()
        font3.setFamily(u"Consolas")
        font3.setPointSize(10)
        self.label_credits_2.setFont(font3)
        self.label_credits_2.setStyleSheet(u"color: rgba(239, 0, 156, 255);\n"
"background-color: rgba(255, 255, 255, 0); ")
        self.label_credits_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_credits_3 = QLabel(self.dropShadowFrame)
        self.label_credits_3.setObjectName(u"label_credits_3")
        self.label_credits_3.setGeometry(QRect(230, 10, 141, 21))
        self.label_credits_3.setFont(font3)
        self.label_credits_3.setStyleSheet(u"color: rgba(239, 0, 156, 255);\n"
"background-color: rgba(255, 255, 255, 0); ")
        self.label_credits_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_credits_4 = QLabel(self.dropShadowFrame)
        self.label_credits_4.setObjectName(u"label_credits_4")
        self.label_credits_4.setGeometry(QRect(230, 150, 141, 21))
        self.label_credits_4.setFont(font3)
        self.label_credits_4.setStyleSheet(u"color: rgba(239, 0, 156, 255);\n"
"background-color: rgba(255, 255, 255, 0); ")
        self.label_credits_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.passbox = QLineEdit(self.dropShadowFrame)
        self.passbox.setObjectName(u"passbox")
        self.passbox.setGeometry(QRect(230, 180, 161, 20))
        self.login = QPushButton(self.dropShadowFrame)
        self.login.setObjectName(u"login")
        self.login.setGeometry(QRect(230, 260, 75, 23))
        self.login.setFont(font2)
        self.login.setStyleSheet(u"color: rgba(255, 255, 255, 255);\n"
"background-color: rgba(239, 0, 156, 255);")
        self.changelog_3 = QLabel(self.dropShadowFrame)
        self.changelog_3.setObjectName(u"changelog_3")
        self.changelog_3.setGeometry(QRect(410, 50, 241, 231))
        self.changelog_3.setFont(font1)
        self.changelog_3.setStyleSheet(u"color: rgb(3, 198, 252);\n"
"background-color: rgba(255, 255, 255, 0); ")
        self.changelog_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.registerButton = QPushButton(self.dropShadowFrame)
        self.registerButton.setObjectName(u"registerButton")
        self.registerButton.setGeometry(QRect(230, 310, 75, 23))
        self.registerButton.setFont(font2)
        self.registerButton.setStyleSheet(u"color: rgba(255, 255, 255, 255);\n"
"background-color: rgba(239, 0, 156, 255);")
        self.exitButton = QPushButton(self.dropShadowFrame)
        self.exitButton.setObjectName(u"exitButton")
        self.exitButton.setGeometry(QRect(580, 350, 75, 23))
        self.exitButton.setFont(font2)
        self.exitButton.setStyleSheet(u"color: rgba(255, 255, 255, 255);\n"
"background-color: rgba(239, 0, 156, 255);")
        self.response = QLabel(self.dropShadowFrame)
        self.response.setObjectName(u"response")
        self.response.setGeometry(QRect(230, 210, 181, 41))
        self.response.setFont(font3)
        self.response.setStyleSheet(u"color: rgba(239, 0, 156, 255);\n"
"background-color: rgba(255, 255, 255, 0); ")
        self.response.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.changePW = QPushButton(self.dropShadowFrame)
        self.changePW.setObjectName(u"changePW")
        self.changePW.setGeometry(QRect(470, 350, 101, 23))
        self.changePW.setFont(font2)
        self.changePW.setStyleSheet(u"color: rgba(255, 255, 255, 255);\n"
"background-color: rgba(239, 0, 156, 255);")

        self.verticalLayout.addWidget(self.dropShadowFrame)

        main.setCentralWidget(self.centralwidget)

        self.retranslateUi(main)

        QMetaObject.connectSlotsByName(main)
    # setupUi

    def retranslateUi(self, main):
        main.setWindowTitle(QCoreApplication.translate("main", u"Tsar", None))
        self.label_title.setText(QCoreApplication.translate("main", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Tsar</span></p></body></html>", None))
        self.label_credits.setText(QCoreApplication.translate("main", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Created</span><span style=\" font-size:12pt;\">: enigmapr0ject</span></p></body></html>", None))
        self.changelog.setText(QCoreApplication.translate("main", u"<html><head/><body><p><span style=\" font-size:10pt; text-decoration: underline;\">1.0.1:</span></p><p><span style=\" font-size:10pt;\">-Draggable windows<br/>-KDE blur Support</span></p><p><span style=\" font-size:10pt; text-decoration: underline;\">To Come:</span></p><p><span style=\" font-size:10pt;\">-UNIX universal blur</span></p><p><span style=\" font-size:10pt;\">-Additional functionality</span></p><p><br/></p></body></html>", None))
        self.changelog_2.setText(QCoreApplication.translate("main", u"<html><head/><body><p><span style=\" font-size:10pt;\">To keep up to date with</span></p><p><span style=\" font-size:10pt;\">all latest news and features,</span></p><p><span style=\" font-size:10pt;\">head to our GitHub!</span></p></body></html>", None))
        self.github.setText(QCoreApplication.translate("main", u"GitHub", None))
        self.label_credits_2.setText(QCoreApplication.translate("main", u"<html><head/><body><p>Username</p></body></html>", None))
        self.label_credits_3.setText(QCoreApplication.translate("main", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; font-style:italic;\">Login</span></p></body></html>", None))
        self.label_credits_4.setText(QCoreApplication.translate("main", u"<html><head/><body><p>Password</p></body></html>", None))
        self.passbox.setInputMask("")
        self.passbox.setText("")
        self.login.setText(QCoreApplication.translate("main", u"Log in", None))
        self.changelog_3.setText(QCoreApplication.translate("main", u"<html><head/><body><p><img src=\":/icon/iconfile.ico\"/></p></body></html>", None))
        self.registerButton.setText(QCoreApplication.translate("main", u"Register", None))
        self.exitButton.setText(QCoreApplication.translate("main", u"Exit", None))
        self.response.setText(QCoreApplication.translate("main", u"<html><head/><body><p><br/></p></body></html>", None))
        self.changePW.setText(QCoreApplication.translate("main", u"Change Password", None))
    # retranslateUi

