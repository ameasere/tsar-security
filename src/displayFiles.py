# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DisplayZIP.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import assets_rc

class Ui_displayArchiveGUI(object):
    def setupUi(self, displayArchiveGUI):
        if not displayArchiveGUI.objectName():
            displayArchiveGUI.setObjectName(u"displayArchiveGUI")
        displayArchiveGUI.resize(590, 369)
        icon = QIcon()
        icon.addFile(u"iconfile.ico", QSize(), QIcon.Normal, QIcon.Off)
        displayArchiveGUI.setWindowIcon(icon)
        self.centralwidget = QWidget(displayArchiveGUI)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.dropShadowFrame = QFrame(self.centralwidget)
        self.dropShadowFrame.setObjectName(u"dropShadowFrame")
        self.dropShadowFrame.setStyleSheet(u"QFrame {	\n"
"	background-color: rgba(255, 255, 255, .15);  \n"
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
        self.label_credits.setGeometry(QRect(360, 0, 201, 41))
        self.label_credits.setFont(font)
        self.label_credits.setStyleSheet(u"color: rgba(239, 0, 156, 255);\n"
"background-color: rgba(255, 255, 255, 0); ")
        self.label_credits.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_credits_3 = QLabel(self.dropShadowFrame)
        self.label_credits_3.setObjectName(u"label_credits_3")
        self.label_credits_3.setGeometry(QRect(150, 10, 141, 21))
        font1 = QFont()
        font1.setFamily(u"Consolas")
        font1.setPointSize(10)
        self.label_credits_3.setFont(font1)
        self.label_credits_3.setStyleSheet(u"color: rgba(239, 0, 156, 255);\n"
"background-color: rgba(255, 255, 255, 0); ")
        self.label_credits_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.closeButton = QPushButton(self.dropShadowFrame)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setGeometry(QRect(470, 320, 91, 23))
        font2 = QFont()
        font2.setFamily(u"Consolas")
        self.closeButton.setFont(font2)
        self.closeButton.setStyleSheet(u"color: rgba(255, 255, 255, 255);\n"
"background-color: rgba(239, 0, 156, 255);")
        self.response = QLabel(self.dropShadowFrame)
        self.response.setObjectName(u"response")
        self.response.setGeometry(QRect(230, 210, 181, 41))
        self.response.setFont(font1)
        self.response.setStyleSheet(u"color: rgba(239, 0, 156, 255);\n"
"background-color: rgba(255, 255, 255, 0); ")
        self.response.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.feedback = QLabel(self.dropShadowFrame)
        self.feedback.setObjectName(u"feedback")
        self.feedback.setGeometry(QRect(320, 50, 231, 181))
        self.feedback.setFont(font1)
        self.feedback.setStyleSheet(u"color: rgba(3, 198, 252, 255);\n"
"background-color: rgba(255, 255, 255, 0); ")
        self.feedback.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.contentsLabel = QLabel(self.dropShadowFrame)
        self.contentsLabel.setObjectName(u"contentsLabel")
        self.contentsLabel.setGeometry(QRect(10, 50, 301, 291))
        self.contentsLabel.setFont(font1)
        self.contentsLabel.setStyleSheet(u"color: rgba(3, 198, 252, 255);\n"
"background-color: rgba(255, 255, 255, 0); ")
        self.contentsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout.addWidget(self.dropShadowFrame)

        displayArchiveGUI.setCentralWidget(self.centralwidget)

        self.retranslateUi(displayArchiveGUI)

        QMetaObject.connectSlotsByName(displayArchiveGUI)
    # setupUi

    def retranslateUi(self, displayArchiveGUI):
        displayArchiveGUI.setWindowTitle(QCoreApplication.translate("displayArchiveGUI", u"Tsar", None))
        self.label_title.setText(QCoreApplication.translate("displayArchiveGUI", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Tsar</span></p></body></html>", None))
        self.label_credits.setText(QCoreApplication.translate("displayArchiveGUI", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Created</span><span style=\" font-size:12pt;\">: enigmapr0ject</span></p></body></html>", None))
        self.label_credits_3.setText(QCoreApplication.translate("displayArchiveGUI", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; font-style:italic;\">Display Files</span></p></body></html>", None))
        self.closeButton.setText(QCoreApplication.translate("displayArchiveGUI", u"Close", None))
        self.response.setText(QCoreApplication.translate("displayArchiveGUI", u"<html><head/><body><p><br/></p></body></html>", None))
        self.feedback.setText(QCoreApplication.translate("displayArchiveGUI", u"<html><head/><body><p><br/></p></body></html>", None))
        self.contentsLabel.setText(QCoreApplication.translate("displayArchiveGUI", u"<html><head/><body><p><br/></p></body></html>", None))
    # retranslateUi

