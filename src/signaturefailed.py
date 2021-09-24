# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SignatureFailed.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_FailedScreen2(object):
    def setupUi(self, FailedScreen2):
        if not FailedScreen2.objectName():
            FailedScreen2.setObjectName(u"FailedScreen2")
        FailedScreen2.resize(680, 371)
        self.centralwidget = QWidget(FailedScreen2)
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
        self.subtitle.setGeometry(QRect(0, 100, 661, 171))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(14)
        self.subtitle.setFont(font1)
        self.subtitle.setStyleSheet(u"color: rgba(239, 0, 156, 255);\n"
"background-color: rgba(255, 255, 255, 0); ")
        self.subtitle.setAlignment(Qt.AlignCenter)
        self.credit = QLabel(self.dropShadowFrame)
        self.credit.setObjectName(u"credit")
        self.credit.setGeometry(QRect(30, 330, 621, 21))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(10)
        self.credit.setFont(font2)
        self.credit.setStyleSheet(u"color: rgba(239, 0, 156, 255);\n"
"background-color: rgba(255, 255, 255, 0); ")
        self.credit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.exitButton = QPushButton(self.dropShadowFrame)
        self.exitButton.setObjectName(u"exitButton")
        self.exitButton.setGeometry(QRect(420, 300, 75, 23))
        self.exitButton.setStyleSheet(u"color: rgba(255, 255, 255, 255);\n"
"background-color: rgba(239, 0, 156, 255);")
        self.continueButton = QPushButton(self.dropShadowFrame)
        self.continueButton.setObjectName(u"continueButton")
        self.continueButton.setGeometry(QRect(300, 300, 75, 23))
        self.continueButton.setStyleSheet(u"color: rgba(255, 255, 255, 255);\n"
"background-color: rgba(239, 0, 156, 255);")
        self.updateButton = QPushButton(self.dropShadowFrame)
        self.updateButton.setObjectName(u"updateButton")
        self.updateButton.setGeometry(QRect(180, 300, 75, 23))
        self.updateButton.setStyleSheet(u"color: rgba(255, 255, 255, 255);\n"
"background-color: rgba(239, 0, 156, 255);")

        self.verticalLayout.addWidget(self.dropShadowFrame)

        FailedScreen2.setCentralWidget(self.centralwidget)

        self.retranslateUi(FailedScreen2)

        QMetaObject.connectSlotsByName(FailedScreen2)
    # setupUi

    def retranslateUi(self, FailedScreen2):
        FailedScreen2.setWindowTitle(QCoreApplication.translate("FailedScreen2", u"SoarGuide", None))
        self.title.setText(QCoreApplication.translate("FailedScreen2", u"<html><head/><body><p><span style=\" font-weight:600;\">Signature Failed</span></p></body></html>", None))
        self.subtitle.setText(QCoreApplication.translate("FailedScreen2", u"<html><head/><body><p>You are currently running an outdated version of Tsar. </p><p>This means you are vulnerable to bugs, security flaws and other open holes </p><p>that have been plugged in recent updates. Tsar will continue to function, </p><p>however you will not be able to access new features and patches </p><p>until you update.</p></body></html>", None))
        self.credit.setText(QCoreApplication.translate("FailedScreen2", u"<strong>Created</strong>: enigmapr0ject", None))
        self.exitButton.setText(QCoreApplication.translate("FailedScreen2", u"Exit", None))
        self.continueButton.setText(QCoreApplication.translate("FailedScreen2", u"Continue", None))
        self.updateButton.setText(QCoreApplication.translate("FailedScreen2", u"Update", None))
    # retranslateUi

