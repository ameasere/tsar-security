# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'extractArchive.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import assets_rc

class Ui_extractArchiveGUI(object):
    def setupUi(self, extractArchiveGUI):
        if not extractArchiveGUI.objectName():
            extractArchiveGUI.setObjectName(u"extractArchiveGUI")
        extractArchiveGUI.resize(590, 219)
        icon = QIcon()
        icon.addFile(u"iconfile.ico", QSize(), QIcon.Normal, QIcon.Off)
        extractArchiveGUI.setWindowIcon(icon)
        self.centralwidget = QWidget(extractArchiveGUI)
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
        self.label_credits.setGeometry(QRect(360, 0, 201, 41))
        self.label_credits.setFont(font)
        self.label_credits.setStyleSheet(u"color: rgba(239, 0, 156, 255);\n"
"background-color: rgba(255, 255, 255, 0); ")
        self.label_credits.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_credits_3 = QLabel(self.dropShadowFrame)
        self.label_credits_3.setObjectName(u"label_credits_3")
        self.label_credits_3.setGeometry(QRect(150, 10, 151, 21))
        font1 = QFont()
        font1.setFamily(u"Consolas")
        font1.setPointSize(10)
        self.label_credits_3.setFont(font1)
        self.label_credits_3.setStyleSheet(u"color: rgba(239, 0, 156, 255);\n"
"background-color: rgba(255, 255, 255, 0); ")
        self.label_credits_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.closeButton = QPushButton(self.dropShadowFrame)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setGeometry(QRect(10, 170, 91, 23))
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
        self.selectArchiveButton = QPushButton(self.dropShadowFrame)
        self.selectArchiveButton.setObjectName(u"selectArchiveButton")
        self.selectArchiveButton.setGeometry(QRect(10, 60, 91, 23))
        self.selectArchiveButton.setFont(font2)
        self.selectArchiveButton.setStyleSheet(u"color: rgba(255, 255, 255, 255);\n"
"background-color: rgba(3, 198, 252, 255);")
        self.extractArchiveButton = QPushButton(self.dropShadowFrame)
        self.extractArchiveButton.setObjectName(u"extractArchiveButton")
        self.extractArchiveButton.setGeometry(QRect(10, 100, 91, 23))
        self.extractArchiveButton.setFont(font2)
        self.extractArchiveButton.setStyleSheet(u"color: rgba(255, 255, 255, 255);\n"
"background-color: rgba(239, 0, 156, 255);")
        self.feedback = QLabel(self.dropShadowFrame)
        self.feedback.setObjectName(u"feedback")
        self.feedback.setGeometry(QRect(150, 60, 401, 131))
        self.feedback.setFont(font1)
        self.feedback.setStyleSheet(u"color: rgba(3, 198, 252, 255);\n"
"background-color: rgba(255, 255, 255, 0); ")
        self.feedback.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout.addWidget(self.dropShadowFrame)

        extractArchiveGUI.setCentralWidget(self.centralwidget)

        self.retranslateUi(extractArchiveGUI)

        QMetaObject.connectSlotsByName(extractArchiveGUI)
    # setupUi

    def retranslateUi(self, extractArchiveGUI):
        extractArchiveGUI.setWindowTitle(QCoreApplication.translate("extractArchiveGUI", u"Tsar", None))
        self.label_title.setText(QCoreApplication.translate("extractArchiveGUI", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Tsar</span></p></body></html>", None))
        self.label_credits.setText(QCoreApplication.translate("extractArchiveGUI", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Created</span><span style=\" font-size:12pt;\">: enigmapr0ject</span></p></body></html>", None))
        self.label_credits_3.setText(QCoreApplication.translate("extractArchiveGUI", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; font-style:italic;\">Extract Archive</span></p></body></html>", None))
        self.closeButton.setText(QCoreApplication.translate("extractArchiveGUI", u"Close", None))
        self.response.setText(QCoreApplication.translate("extractArchiveGUI", u"<html><head/><body><p><br/></p></body></html>", None))
        self.selectArchiveButton.setText(QCoreApplication.translate("extractArchiveGUI", u"Select Archive", None))
        self.extractArchiveButton.setText(QCoreApplication.translate("extractArchiveGUI", u"Extract Archive", None))
        self.feedback.setText(QCoreApplication.translate("extractArchiveGUI", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
    # retranslateUi

